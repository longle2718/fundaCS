# Strings related utilities.
#
# Long Le <longle1@illinois.edu>
# University of Illinois
#

import numpy as np

# compute the Levenshtein distance between
# two strings using Wagner-Fischer algorithm
def levenshteinDist(a,b):
    aN = len(a)
    bN = len(b)
    D = np.zeros((aN,bN))
    for k in range(aN):
        for l in range(bN):
            if min(k,l) == 0:
                D[k,l] = max(k,l) # deletion/insertion
            else:
                if a[k-1] != b[l-1]:
                    ind = 1
                else:
                    ind = 0
                D[k,l] = min([D[k-1,l]+1, # deletion
                              D[k,l-1]+1, # insertion
                              D[k-1,l-1]+ind]) # substitution
    return D[aN-1,bN-1] 

#The common template for substring problems.
#Inspired by Dijkstra.
'''
def findSubstring(s):
    cntMap = {} # check whether the substring is valid
    # the analog of initializing the queue
    for c in s:
        cntMap[c] = 0
    cnt = 0

    begin = 0
    end = 0
    d = 0
    while end < len(s):
        # the analog of dequeuing
        if cntMap[s[end]]:
            # modify cnt here
        cntMap[s[end]] -= 1
        end += 1

        # the analog of getting neighbor nodes
        while: # cnt condition
            # update d here if finding minimum

            # the analog of enqueuing
            # increase begin to make it invalid/valid again
            if cntMap[s[begin]]:
                # modify cnt here
            cntMap[s[begin]] += 1
            begin += 1

        # update d here if finding maximum

    return d
'''
def anagramSubstr(s,p):
    rv = []
    if s==None or len(s)==0 or p==None or len(p)==0:
        return rv

    # initialize the hash map here
    # character-to-the diff in the # of occurrences between p and s[begin:end]
    cntMap = {}
    for c in s:
        cntMap[c] = 0
    for c in p:
        cntMap[c] = 0
    for c in p:
        cntMap[c] += 1
    cnt = len(p) # check if the substring is valid

    begin = 0 # head pointer
    end = 0 # tail pointer
    while end < len(s):
        # the analog of dequeuing
        # move right everytime, if the character exists in p's hash, decrease the cnt
        # current hash value >= 1 means the character is existing in p
        if cntMap[s[end]] >= 1:
            # modify cnt here
            cnt -= 1
        cntMap[s[end]] -= 1
        end += 1

        # when the cnt is down to 0, means we found the right anagram
        # then add window's left to result list
        if cnt == 0:
            rv.append(begin)

        # if we find the window's size equals to p, then we have to move left 
        #(narrow the window) to find the new match window
        if end - begin == len(p):
            # the analog of enqueuing
            # must undo if applicable
            # notice that cnt is incremented/decremented only once at the boundary of 1/0
            if cntMap[s[begin]] >= 0:
                # only increase the cnt if the character is in p
                # the cnt >= 0 indicate it was original in the hash, cuz it won't go below 0
                cnt += 1

            # ++ to reset the hash because we kicked it out the left
            cntMap[s[begin]] += 1
            begin += 1

    return rv
