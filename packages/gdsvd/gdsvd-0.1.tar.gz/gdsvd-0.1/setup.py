from setuptools import setup, find_packages

setup(
    name='gdsvd',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ],
    author='Emily Gan',
    author_email='emily.gan496@gmail.com',
    description='A package for gradient-based SVD',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/matrix-completion/gdsvd',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)