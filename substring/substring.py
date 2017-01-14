'''
Substrings related utilities.
The common template.

def findSubstring(s):
    cntMap = {}
    for c in s:
        cntMap[c] = 0
    cnt = 0

    begin = 0
    end = 0
    d = 0
    while end < len(s):
        if cntMap[s[end]]:
            # modify cnt here
        cntMap[s[end]] -= 1
        end += 1

        while: # cnt condition
            # update d here if finding minimum
            # increase begin to make it invalid/valid again
            if cntMap[s[begin]]:
                # modify cnt here
            cntMap[s[begin]] += 1
            begin += 1

        # update d here if finding maximum

    return d

Long Le <longle1@illinois.edu>
University of Illinois
'''

def anagramSubstr(s,p):
    rv = []
    if s==None or len(s)==0 or p==None or len(p)==0:
        return rv

    # initialize the hash map here
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
            if cntMap[s[begin]] >= 0:
                # only increase the cnt if the character is in p
                # the cnt >= 0 indicate it was original in the hash, cuz it won't go below 0
                cnt += 1

            # ++ to reset the hash because we kicked it out the left
            cntMap[s[begin]] += 1
            begin += 1

    return rv
