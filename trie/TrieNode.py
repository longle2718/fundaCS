# Trie (Prefix Tree) Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
import os,sys
sys.path.append(os.path.expanduser('~')+'/randProbs/graphSearch')
sys.path.append('..//graphSearch')
from GraphNode import add_arrow

class TrieNode:
    def __init__(self,val):
        self.val = val # accumulated edge char
        self.childMap = {} # char to child node map

# Further optimization is available as a
# deterministic acyclic finite state automaton (DAFSA).
# Implementation details are given in:
#
# Jan Daciuk, Stoyan Mihov, Bruce Watson and Richard Watson (2000).
# Incremental construction of minimal acyclic finite state automata.
# Computational Linguistics 26(1):3-16.
#
def buildTrie(words):
    root = TrieNode('$') # required dummy node

    for word in words:
        node = root
        for i in range(len(word)):
            if word[i] not in node.childMap:
                node.childMap[word[i]] = TrieNode(word[:i+1])
            node = node.childMap[word[i]]

    return root

