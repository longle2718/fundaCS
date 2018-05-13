'''
Utility functions for multi-scale representation (MSR) or
multiresolution analysis (MRA)

Long Le <longle1@illinois.edu>
University of Illinois
'''

import numpy as np
import cv2
import pywt

def imPyrshow(pyramid):
    if len(pyramid) == 0:
        return None

    rows,cols = np.shape(pyramid[0])
    composite_image = np.zeros((rows, cols + cols // 2), dtype=np.double)
    composite_image[:rows, :cols] = pyramid[0]
    i_row = 0

    for p in pyramid[1:]:
        n_rows, n_cols = p.shape[:2]
        composite_image[i_row:i_row + n_rows, cols:cols + n_cols] = p
        i_row += n_rows

    return composite_image

def gaussian_pyr(imGray,level=2):
    im = imGray.copy()
    gp = [im]
    for k in range(level-1):
        im = cv2.pyrDown(im)
        gp.append(im)
    return gp

def laplacian_pyr(imGray,level=2):
    gp = gaussian_pyr(imGray,level)

    lp = [gp[level-1]]
    for k in range(level-1,0,-1):
        ge = cv2.pyrUp(gp[k]) # Gaussian estimate
        L = cv2.subtract(gp[k-1],ge)
        lp.append(L)

    lp = lp[::-1]
    return lp
