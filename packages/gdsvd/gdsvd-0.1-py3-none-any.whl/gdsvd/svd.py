"""Module providing a rank-SVD implementations."""

import os
import numpy as np
from .utils import *

##########################
## Gradient computation ##
##########################

def compute_gradient_x(M_l, U, Vt, l, x, m, n):
    '''
    Computes the gradient of the loss function with respect to x
    
    @param M: np array of shape (m, n), input matrix
    @param U: np array of shape (m, rank), left singular column vectors
    @param Vt: np array of shape (rank, n), right singular column vectors
    @param l: current rank being computed
    @param x: np array of shape (m,1)
    @param m: # of rows in M
    @param n: # of cols in M
    @return: np array of shape (m,1)
    '''
    compute_MT_x(n, M_l, x, Vt[l:l+1,:])
    compute_M_x(m, M_l, Vt[l:l+1,:], U[:,l:l+1])
    return x - (1/np.linalg.norm(x)**2) * U[:,l:l+1]

##########################
##    Power Method
##########################
def power_method(M,
                rank = 1,
                eps = 1e-9,
                record_conv = False,
                U_true = None,
                S_true = None,
                Vt_true = None
                ):
    '''
    Computes rank-SVD via power method
    
    @param M: np array of shape (m, n), matrix that is being approximated with singular values
    @param rank: int, rank of the approximation
    @param max_iters: int, max number of steps to run algorithm fol+1)
    @param eps: float, tolerance for stopping condition
    @param record_conv: bool, whether to record convergence metrics (slows down computation)
    @param U_true: np array of shape (m, rank), true left singular vectors
    @param S_true: np array of shape (rank,), true singular values
    @param Vt_true: np array of shape (rank, n), true right singular vectors

    @return: U (m, rank), S (rank,), Vt (rank, n), record (list of tab separated strings, first line is convergence iters, second is header)
    '''
    # initialize U, S, Vt
    m,n = M.shape
    S = np.ones(rank)
    U = np.random.rand(m, rank)
    Vt = np.random.rand(rank, n)

    record = [np.zeros(rank, dtype = int),"rank\titer\tMerr\tSerr\tstepsize\tUerr\tU_ortho\tU_norm\tVerr\tV_ortho\tV_norm"]

    # initialize M_l
    M_l = np.memmap("_svd_M_l_temp.dat", dtype=np.float64, mode='w+', shape=(m,n))
    np.copyto(M_l, M)

    for l in range(rank):
        # normalize U, Vt
        U[:,l:l+1] /= np.linalg.norm(U[:,l:l+1])
        Vt[l:l+1,:] /= np.linalg.norm(Vt[l:l+1,:])

        # initialize convergence conditions
        eps_1 = 1
        eps_2 = 1

        while (eps_1 > eps) or (eps_2 > eps):
            eps_1 = U[:,l:l+1].copy()
            eps_2 = Vt[l:l+1,:].copy()
            
            # compute update for u
            compute_M_x(m, M_l, Vt[l:l+1,:], U[:,l:l+1])

            # compute update for vT
            compute_MT_x(n, M_l, U[:,l:l+1], Vt[l:l+1,:])

            # update singular value/vectors
            S[l] = np.linalg.norm(U[:,l:l+1])
            U[:,l:l+1] /= np.linalg.norm(U[:,l:l+1])
            Vt[l:l+1,:] /= np.linalg.norm(Vt[l:l+1,:])

            # compute stopping conditions
            eps_1 = np.linalg.norm(U[:,l:l+1] - eps_1)
            eps_2 = np.linalg.norm(Vt[l:l+1,:] - eps_2)

            if record_conv:
                record.append(f"{l+1}\t{record[0][l]}\t{M_err(M, U, S, Vt)}\t{S_err(S, S_true, l+1)}\t{eps_1+eps_2}\t{U_err(U, U_true, l+1)}\t{U_ortho(U)}\t{np.linalg.norm(U[:,l:l+1])}\t{Vt_err(Vt, Vt_true, l+1)}\t{Vt_ortho(Vt)}\t{np.linalg.norm(Vt[l:l+1,:])}")

            record[0][l] +=1

        M_l -= U[:,l:l+1] @ np.diag(S[l:l+1]) @ Vt[l:l+1,:]
        M_l.flush()
    
    os.remove("_svd_M_l_temp.dat")
    if record_conv:
        return U,S,Vt, record
    else:
        return U,S,Vt

##########################
##  SVD via Gradient Descent
##########################
def gd_svd(M,
            rank = 1,
            eps = 1e-9,
            eta = 1/2,
            record_conv = False,
            U_true = None,
            S_true = None,
            Vt_true = None,
            ):
    '''
    Computes rank-SVD via gradient descent
    
    @param M: np array of shape (m, n), matrix that is being approximated with singular values
    @param rank: int, rank of the approximation
    @param max_iters: int, max number of steps to run algorithm for)
    @param eps: float, tolerance for stopping condition
    @param record_conv: bool, whether to record convergence metrics (slows down computation)
    @param U_true: np array of shape (m, rank), true left singular vectors
    @param S_true: np array of shape (rank,), true singular values
    @param Vt_true: np array of shape (rank, n), true right singular vectors

    @return: U (m, rank), S (rank,), Vt (rank, n), record (list of tab separated strings, first line is convergence iters, second is header)
    '''
    # initialize U, S, Vt, x
    m,n = M.shape
    x = np.zeros(shape=(m,1))
    U = np.zeros(shape=(m, rank))
    S = np.ones(rank)
    Vt = np.random.rand(rank, n)

    record = [np.zeros(rank, dtype = int), "rank\titer\tMerr\tSerr\tstepsize\tUerr\tU_ortho\tU_norm\tVerr\tV_ortho\tV_norm"]

    # initialize M_l
    M_l = np.memmap("_svd_M_l_temp.dat", dtype=np.float64, mode='w+', shape=(m,n))
    np.copyto(M_l, M)

    for l in range(rank):
        # normalize Vt
        Vt[l:l+1,:] /= np.linalg.norm(Vt[l:l+1,:])

        # initialize x
        compute_M_x(m, M_l, Vt[l:l+1,:], x)

        # initialize gradient
        grad_x = np.ones_like(x)

        while np.linalg.norm(grad_x) > eps:
            # compute gradient of x
            grad_x = compute_gradient_x(M_l, U, Vt, l, x, m, n)
            
            # step x
            x -= eta * grad_x

            # update singular value/vectors
            S[l] = np.linalg.norm(x)
            U[:,l:l+1] = x/np.linalg.norm(x)
            Vt[l:l+1,:] /= np.linalg.norm(x)**2

            if record_conv:
                record.append(f"{l+1}\t{record[0][l]}\t{M_err(M, U, S, Vt)}\t{S_err(S, S_true, l+1)}\t{eta*np.linalg.norm(grad_x)}\t{U_err(U, U_true, l+1)}\t{U_ortho(U)}\t{np.linalg.norm(U[:,l:l+1])}\t{Vt_err(Vt, Vt_true, l+1)}\t{Vt_ortho(Vt)}\t{np.linalg.norm(Vt[l:l+1,:])}")
            
            record[0][l] +=1

        M_l -= U[:,l:l+1] @ np.diag(S[l:l+1]) @ Vt[l:l+1,:]
        M_l.flush()
    
    # remove temporary file
    os.remove("_svd_M_l_temp.dat")
    if record_conv:
        return U,S,Vt, record
    else:
        return U,S,Vt