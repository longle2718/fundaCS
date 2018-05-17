class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        prev = {} # word->prev word
        prev[beginWord] = None
        
        exploring = [] # exploring queue
        exploring.append(beginWord)
        exploringCost = [] # exploring cost so far
        exploringCost.append(0)
        
        explored = set() # explored queue
        
        while len(exploring) > 0:
            # dequeue
            popIdx = exploringCost.index(min(exploringCost))
            cost_cur = exploringCost.pop(popIdx)
            word_cur = exploring.pop(popIdx)
            if word_cur == endWord:
                break
            
            # enqueue
            explored.add(word_cur)
            
            # exploring neighbors
            for word in wordList:
                if word not in explored and self.isNeighbor(word,word_cur):
                    if word not in exploring:
                        exploring.append(word)
                        exploringCost.append(cost_cur+1)
                        prev[word] = [word_cur]
                    else:
                        idx = exploring.index(word)
                        if exploringCost[idx] > cost_cur+1:
                            exploringCost[idx] = cost_cur+1
                            prev[word] = [word_cur]
                        elif exploringCost[idx] == cost_cur+1:
                            prev[word].append(word_cur)
        
        return self.getSeq(endWord,prev)
            
    def getSeq(self,endWord,prevSrc):
        prev = dict(prevSrc)
        #print('prev = %s' % prev)
        
        # list of all seqs
        seqList = []
        
        seqQueue = []
        seqQueue.append([])
        while len(seqQueue) > 0:
            seq = seqQueue.pop()
            # back track for a seq
            if len(seq) == 0:
                word_cur = endWord
            else:
                word_cur = seq.pop()
            while True:
                if word_cur not in prev:
                    break
                else:
                    seq.append(word_cur)
                    if prev[word_cur] is None:
                        break
                    elif len(prev[word_cur]) == 1:
                        word_cur = prev[word_cur][0]
                    elif len(prev[word_cur]) > 1:
                        seqQueue.append(list(seq))
                        word_cur = prev[word_cur].pop(0)
                        #print('prev = %s' % prev)
                    
            if len(seq) > 0:
                seqList.append(seq)
        
        for k in range(len(seqList)):
            seqList[k] = seqList[k][::-1]
            
        return seqList
        
    def isNeighbor(self,word1,word2):
        if self.dist(word1,word2) == 1:
            return True
        else:
            return False
    
    def dist(self,word1,word2):
        N1 = len(word1)
        N2 = len(word2)
        
        dist = 0
        for k in range(min(N1,N2)):
            if word1[k] != word2[k]:
                dist += 1
        dist += max(N1,N2)-min(N1,N2)
        
        return dist
        