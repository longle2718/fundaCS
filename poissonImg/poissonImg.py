'''
Poisson Image Editing / Gradient domain processing

Long Le <longle2718@gmail.com>
'''

import numpy as np
import scipy
from scipy.sparse import linalg as linalg
#from scipy.sparse import csr_matrix as csr_matrix
from scipy.sparse import lil_matrix as lil_matrix

'''
Image reconstruction from gradient images by solving a Poisson 
equation (https://github.com/willemmanuel/poisson-image-editing).
Related work:
Directly solving the gradient least square formulation 
(https://www.mathworks.com/matlabcentral/fileexchange/9734-inverse-integrated-gradient?focused=3773008&tab=function).
'''
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
    composite = np.copy(dst)
    # Place new estimate in dst on mask
    for i,p in enumerate(ps_mask):
        # ensure valid solutions
        composite[p] = min(1,max(0,x[0][i]))
    return composite

'''
Inverse gradient image via DST (http://www.amitkagrawal.com/cvpr06/EdgeSuppression.html).
Related work:
Convolution pyramids (http://www.cs.huji.ac.il/labs/cglab/projects/convpyr/).
'''
def imgradient(im):
    gx = np.zeros(im.shape)
    '''
    for k in range(im.shape[0]):
        for l in range(im.shape[1]-1):
            gx[k,l] = im[k,l+1] - im[k,l]
    '''
    gx[:,:-1] = im[:,1:] - im[:,:-1]

    gy = np.zeros(im.shape)
    '''
    for k in range(im.shape[0]-1):
        for l in range(im.shape[1]):
            gy[k,l] = im[k+1,l] - im[k,l]
    '''
    gy[:-1,:] = im[1:,:] - im[:-1,:]

    return gx,gy

def invgrad(gx,gy,im_bdry):
    # laplacian
    H,W = gx.shape
    gyy = np.zeros((H,W))
    gxx = np.zeros((H,W))
    '''
    for k in range(H-1):
        for l in range(W-1):
            gyy[k+1,l] = gy[k+1,l] - gy[k,l]
            gxx[k,l+1] = gx[k,l+1] - gx[k,l]
    '''
    gyy[1:,:-1] = gy[1:,:-1] - gy[:-1,:-1] 
    gxx[:-1,1:] = gx[:-1,1:] - gx[:-1,:-1] 
    f = gxx + gyy
    #print('f.shape = %s' % (f.shape,))

    # zero out unused part of the boundary image
    im_bdry[1:-1,1:-1] = 0
    f_bp = np.zeros((H,W))
    for k in range(1,H-1):
        for l in range(1,W-1):
            f_bp[k,l] = -4*im_bdry[k,l]+im_bdry[k,l+1]+im_bdry[k,l-1]+im_bdry[k+1,l]+im_bdry[k-1,l]
    #print('f_bp.shape = %s' % (f_bp.shape,))
    
    # subtract boundary points contribution
    f = f - f_bp
    #print('f.shape = %s' % (f.shape,))

    f = f[1:-1,1:-1]
    #print('f.shape = %s' % (f.shape,))

    # DST algo starts
    # compute sine transform
    F = dst(f)
    F = dst(F.T).T
    #print('F.shape = %s' % (F.shape,))

    # compute eigen values
    x,y = np.meshgrid(np.arange(1,W-1),np.arange(1,H-1))
    #print('x.shape = %s' % (x.shape,))
    #print('y.shape = %s' % (y.shape,))
    denom = 2*np.cos(np.pi*x/(W-1))-2 + 2*np.cos(np.pi*y/(H-1))-2
    #print('denom.shape = %s' % (denom.shape,))
    # normalize
    F = F/denom

    # compute inverse sine transform
    f = idst(F)
    f = idst(f.T).T

    # put solution in inner points; outer points obtained from boundary image
    im_out = im_bdry
    im_out[1:-1,1:-1] = np.maximum(0,np.minimum(255,f))
    
    return im_out

def dst(a):
    n,m = a.shape

    y = np.zeros((2*(n+1),m))
    y[1:n+1,:] = a
    y[n+2:2*n+2,:] = -np.flipud(a)

    yy = np.fft.fft(y,axis=0)
    b = yy[1:n+1,:]/(-2j)
    b  = np.real(b)
    return b
   
def idst(a):
    n = a.shape[0]
    nn = n+1
    b = 2./nn*dst(a)
    return b
