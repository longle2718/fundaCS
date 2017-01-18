# Bit manipulation utilities
#
# Long Le
# University of Illinois
#

def reverseBits(x):
    mask = 1
    rx = 0
    for k in range(16):
        #print('k = '+str(k))
        #print('mask = '+format(mask,'#018b'))
        #print('mask&x = '+format(mask&x,'#018b'))
        if mask&x != 0:
            rx <<= 1
            rx += 1
        else:
            rx <<= 1
        #print('rx = '+format(rx,'#018b'))

        mask <<= 1

    return rx

def addWithLogic(x,y):
    s = x^y # sum 
    c = x&y # carry out
    while c != 0:
        #print('----------')
        #print('s = '+format(s,'#018b'))
        #print('c = '+format(c,'#018b'))
        sTmp = s^(c<<1)
        cTmp = s&(c<<1)
        s = sTmp
        c = cTmp
    
    return s

def numOf1s(x):
    cnt = 0
    while x != 0:
        cnt += 1
        x = x&(x-1)
    return cnt
