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

def ffs(x):
    # find first set/one
    if x == 0:
        return 0
    mask = 1
    cnt = 1
    while x & mask == 0:
        mask <<= 1
        cnt <<= 1
    return cnt

def ffs_table(x):
    # time-space tradeoff with assistant tables
    if x == 0:
        return 0

    n = 8
    table = [ffs(i) for i in range(2**8)]
    cnt = 0
    while True:
        if x & (2**n-1) != 0:
            return cnt + table[x & (2**n-1)]
        x >>= n
        cnt += n

def ctz(x):
    # count trailing zero == find first set
    # count the # of zeros following the LS 1
    # using de Bruijn sequences
    table = [( 0x077CB531 * (1<<i) ) >> 27 for i in range(32)]
    # x & (-x) isolates the LS 1
    return table[((x & (-x)) * 0x077CB531) >> 27]

def clz(x):
    # count leading zero
    # count the # of zeros preceding the MS 1
    if x == 0:
        return 32

    table = [4, 3, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    while True:
        if x & 0xF0000000 != 0:
            return cnt + table[x >> (32-4)]
        x <<= 4
        cnt += 4

    return
