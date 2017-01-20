# Min heap/priority queue class
#
# Long Le
# University of Illinois
#

class MinHeapQ:
    def __init__(self):
        self.buf = [0]
        self.valMap = {}

    def push(self,key,val):
        # key is an object
        # val is its priority
        self.valMap[key] = val

        self.buf.append(val)
        k = len(self.buf)-1
        while True:
            if self.buf[k] < self.buf[k//2]:
                self.buf[k],self.buf[k//2] = self.buf[k//2],self.buf[k]
                k = k//2
            else:
                break

        return None

    def pop(self):
        rk,_ = self.popitem()
        return rk

    def popitem(self):
        #  extract the root value
        rk = self.buf[1]
        # replace the root with the last value
        self.buf[1] = self.buf.pop()

        # swap with the 'smaller' child
        N = len(self.buf)
        k = 1
        while True:
            if ((2*k+1 < N and self.buf[2*k] < self.buf[k] and self.buf[2*k] < self.buf[2*k+1]) or 
            (2*k < N and 2*k+1 >= N and self.buf[2*k] < self.buf[k])):
                self.buf[k],self.buf[2*k] = self.buf[2*k],self.buf[k]
                k = 2*k
            elif 2*k+1 < N and self.buf[2*k+1] < self.buf[k] and self.buf[2*k+1] < self.buf[2*k]:
                self.buf[k],self.buf[2*k+1] = self.buf[2*k+1],self.buf[k]
                k = 2*k+1
            else:
                break

        rv = self.valMap[rk]
        del self.valMap[rk]

        return rk,rv
        
