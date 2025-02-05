import numpy as np

##########################
##  Tracking metrics    ##
##########################

def M_err(M, U, S, Vt):
    '''
    Computes the ||M - USVt||_F error.
    '''
    return np.linalg.norm(M - U@np.diag(S)@Vt)

def U_ortho(U):
    '''
    Computes the orthogonality of the singular vectors U: ||U.TU - I||_F
    '''
    return np.linalg.norm(U.T@U - np.identity(U.shape[1]))

def U_err(U, U_true, l):
    '''
    Computes the subspace error of the first l singular vectors U compared to U_true: ||UU.T - (U_true)(U_true).T||_F
    '''
    return np.linalg.norm(U[:,:l].T@U[:,:l] - U_true[:,:l].T@U_true[:,:l])

def Vt_ortho(Vt):
    '''
    Computes the orthogonality of the singular vectors Vt: ||(Vt)(Vt).T - I||_F
    '''
    return np.linalg.norm(Vt@Vt.T - np.identity(Vt.shape[0]))

def Vt_err(Vt, Vt_true, l):
    '''
    Computes the subspace error of the first l singular vectors Vt compared to Vt_true: ||(Vt).T(Vt) - (Vt_true).T(Vt_true)||_F
    '''
    return np.linalg.norm(Vt[:l, :].T@Vt[:l, :] - Vt_true[:l, :].T@Vt_true[:l, :])

def S_err(S, S_true, l):
    '''
    Computes the L2 error of the singular values S compared to S_true: ||S - S_true||_2
    '''
    return np.linalg.norm(S[:l]-S_true[:l])

##########################
## Matrix multiplication ##
##########################

def compute_M_lT_x(i, M, U, S, Vt, l, x):
    '''
    Computes M_l.Tx (M_l = M - U_l S_l Vt_l^T)
    
    @param i: index of M.Tx being computed
    @param M: np array of shape (m, n), input matrix
    @param U: np array of shape (m, rank), left singular column vectors
    @param S: np array of shape (rank,), singular values
    @param Vt: np array of shape (rank, n), right singular column vectors
    @param l: current rank being computed
    @param x: np array of shape (m,1)
    @return: np array of shape (1, 1)
    '''
    return (M[:,i:i+1] - U[:,:l] @ np.diag(S[:l]) @ Vt[:l,i:i+1]).T @ x

def compute_M_l_x(i, M, U, S, Vt, l, x):
    '''
    Computes M_lx (M_l = M - U_l S_l Vt_l^T)
    
    @param i: index of Mx being computed
    @param M: np array of shape (m, n), input matrix
    @param U: np array of shape (m, rank), left singular column vectors
    @param S: np array of shape (rank,), singular values
    @param Vt: np array of shape (rank, n), right singular column vectors
    @param l: current rank being computed
    @param x: np array of shape (1, n)
    @return: np array of shape (1, 1)
    '''
    return (M[i:i+1,:] - U[i:i+1,:l]@np.diag(S[:l])@Vt[:l,:]) @ x.T

# parallelized versions

def compute_MT_x_i(i, M, x):
    '''
    Subroutine to compute M.Tx
    
    @param i: index of M.Tx being computed
    @param M: np array of shape (m, n), input matrix
    @param x: np array of shape (m,1)
    @return: np array of shape (1, 1)
    '''
    return M[:,i:i+1].T @ x

def compute_M_x_i(i, M, x):
    '''
    Subroutine to compute Mx
    
    @param i: index of Mx being computed
    @param M: np array of shape (m, n), input matrix
    @param x: np array of shape (1, n)
    @return: np array of shape (1, 1)
    '''
    return M[i:i+1,:] @ x.T

def compute_MT_x(n, M, x, res):
    '''
    Sets res to M.Tx
    
    @param n: int, number of cols in M
    @param M: np array of shape (m, n), input matrix
    @param x: np array of shape (m, 1)
    @param res: np array of shape (1, n)
    @return: np array of shape (1, 1)
    '''
    for i in range(n):
        res[0,i] = compute_MT_x_i(i, M, x).item()

def compute_M_x(m, M, x, res):
    '''
    Sets res to Mx
    
    @param m: int, number of rows in M
    @param M: np array of shape (m, n), input matrix
    @param x: np array of shape (1, n)
    @param res: np array of shape (m,1)
    @return: np array of shape (1, 1)
    '''
    for i in range(m):
        res[i,0] = compute_M_x_i(i, M, x).item()