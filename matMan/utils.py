# Matrix manipulation utilities
#
# Long Le
# University of Illinois
#

def rotateClockwise(mat):
    M = len(mat)
    if M > 0:
        N = len(mat[0])
    else:
        return 

    # reverse up-down
    for k in range(M//2):
        mat[k],mat[M-1-k] = mat[M-1-k],mat[k] 
    # swap along the diagonal axis
    for k in range(len(mat)):
        for l in range(k+1,len(mat)):
            mat[k][l],mat[l][k] = mat[l][k],mat[k][l]
    return

def rotateCounterclockwise(mat):
    M = len(mat)
    if M > 0:
        N = len(mat[0])
    else:
        return 

    # reverse left-right
    for l in range(M):
        for k in range(N//2):
            mat[l][k],mat[l][N-1-k] = mat[l][N-1-k],mat[l][k] 
    # swap along the diagonal axis
    for k in range(len(mat)):
        for l in range(k+1,len(mat)):
            mat[k][l],mat[l][k] = mat[l][k],mat[k][l]
    return
