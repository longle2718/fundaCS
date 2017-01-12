'''
Least-Recent-Used Cache

Long Le <longle1@illinois.edu>
University of Illinois
'''
class LRUCache:
    def __init__(self,capacity):
        self.cap = capacity
        self.valueMap = {}
        self.LRUKeys = []

    def get(self,key):
        if key in self.valueMap:
            self.LRUKeys.remove(key)
            self.LRUKeys.append(key)
            return self.valueMap[key]
        else:
            return -1

    def put(self,key,value):
        if key in self.valueMap:
            self.LRUKeys.remove(key)
        elif len(self.valueMap) >= self.cap:
            del self.valueMap[self.LRUKeys.pop()]

        self.valueMap[key] = value
        self.LRUKeys.append(key)
        return None
