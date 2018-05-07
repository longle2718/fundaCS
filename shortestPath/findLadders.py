class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        dist = {}
        dist[beginWord] = 0
        prev = {}
        prev[beginWord] = None
        
        frontier = []
        frontier.append(beginWord)
        frontierScore = []
        frontierScore.append(0)
        
        explored = set()
        while len(frontier) > 0:
            # dequeue
            popIdx = frontierScore.index(min(frontierScore))
            frontierScore.pop(popIdx)
            word_cur = frontier.pop(popIdx)
            print('word_cur = %s' % word_cur)
            
            # enqueue
            explored.add(word_cur)
            
            # output
            if word_cur == endWord:
                print('endWord reached')
                break
            
            # search neighbors
            for word in wordList:
                if word not in explored and self.isNeighbor(word,word_cur):
                    if word not in dist:
                        dist[word] = dist[word_cur] + 1
                        prev[word] = word_cur
                    else:
                        if dist[word] > dist[word_cur] + 1:
                            dist[word] = dist[word_cur] + 1
                            prev[word] = word_cur

                    frontier.append(word)
                    frontierScore.append(dist[word])
                    
     
        return self.getSeq(endWord,prev)
            
    def getSeq(self,endWord,prev):
        if endWord is None:
            return []
        
        word_cur = endWord
        seq = []
        while True:
            seq.append(word_cur)
            word_cur = prev[word_cur]
            if word_cur is None:
                break
        
        return seq[::-1]
        
    def isNeighbor(self,word1,word2):
        if self.dist(word1,word2) == 1:
            return True
        else:
            return False
        
    def dist(self,word1,word2):
        dist = 0
        N1 = len(word1)
        N2 = len(word2)
        
        for k in range(min(N1,N2)):
            if word1[k] != word2[k]:
                dist += 1;
        dist += max(N1,N2)-min(N1,N2)
        
        return dist
