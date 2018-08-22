'''
Poisson Image Editing

Long Le <longle2718@gmail.com>
'''

import numpy as np
from scipy.sparse import linalg as linalg
#from scipy.sparse import csr_matrix as csr_matrix
from scipy.sparse import lil_matrix as lil_matrix

def mask_pixels(mask):
    nonzero = np.nonzero(mask)
    # zip returns an object in python3
    return list(zip(nonzero[0], nonzero[1]))

def neighbors(p,im):
    M,N = im.shape
    m,n = p
    ngb = []
    if m+1 < M:
        ngb += [(m+1,n)]
    if m-1 >= 0:
        ngb += [(m-1,n)]
    if n+1 < N:
        ngb += [(m,n+1)]
    if n-1 >= 0:
        ngb += [(m,n-1)]
    return ngb 

def in_omega(p, mask):
    # Determine if a given pixel p is either outside or inside omega
    M,N = mask.shape
    m,n = p
    if m < 0 or m >= M or n < 0 or n >= N:
        return False
    return mask[p] == 1

def in_edge(p, mask):
    # Deterimine if a given pixel p is on delta omega (boundary)
    if in_omega(p,mask) == False: return False
    for ngb in neighbors(p,mask):
        # If the point is inside omega, and a surrounding point is not,
        # then we must be on an edge
        if in_omega(ngb,mask) == False: return True
    return False

def laplacian(source,p):
    # Apply the Laplacian operator at a given pixel p
    M,N = source.shape
    i,j = p
    val = 4 * source[i,j]
    if i+1 < M:
        val -= 1 * source[i+1, j]
    if i-1 >= 0:
        val -= 1 * source[i-1, j]
    if j+1 < N:
        val -= 1 * source[i, j+1]
    if j-1 >= 0:
        val -= 1 * source[i, j-1]
    return val

def poisson_sparse_matrix(mask,ps_mask):
    # Create the Laplacian operator A sparse matrix
    # based on a mask

    # N = number of points in mask
    N = len(ps_mask)
    #A = csr_matrix((N,N))
    A = lil_matrix((N,N))
    # Set up row for each point in mask
    for i,p in enumerate(ps_mask):
        # Should have 4's diagonal
        A[i,i] = 4
        # Get all surrounding points
        for ngb in neighbors(p,mask):
            # If a surrounding point is in the mask, add -1 to index's
            # row at correct position
            if ngb not in ps_mask: continue
            j = ps_mask.index(ngb)
            A[i,j] = -1
    return A

def poisson_rhs_vector(src,dst,mask,ps_mask):
    N = len(ps_mask)
    b = np.zeros(N)
    for i,p in enumerate(ps_mask):
        b[i] = laplacian(src,p)
        # handle Dirichlet boundary condition
        if in_edge(p,mask):
            for ngb in neighbors(p,mask):
                if not in_omega(ngb,mask):
                    b[i] += dst[ngb]
    return b 
    

def poisson_clone(src,dst,mask):
    # single channel poisson editting
    ps_mask = mask_pixels(mask)

    A = poisson_sparse_matrix(mask,ps_mask)
    b = poisson_rhs_vector(src,dst,mask,ps_mask)
    x = linalg.cg(A, b)

    # Copy target photo
    composite = np.copy(dst).astype(int)
    # Place new estimate in dst on mask
    for i,p in enumerate(ps_mask):
        composite[p] = x[0][i]
    return composite
