# Graph Node class
#
# Long Le
# University of Illinois
#

import numpy as np
import matplotlib.pyplot as plt
import json

class GraphNode:
    def __init__(self,x):
        self.val = x
        # adjacency list (not matrix) representation
        # directed graph
        self.ngbs = set()

def serialize(nodes):
    # input is an array of GraphNodes
    # node to idx map
    idxMap = {}
    for k,node in enumerate(nodes):
        idxMap[node] = k

    # output is an array of dictionaries
    dicts = []
    for node in nodes:
        idxNgbs = []
        for ngb in node.ngbs:
            idxNgbs.append(idxMap[ngb])

        dicts.append({'val':node.val,'idx':idxMap[node],'idxNgbs':idxNgbs})
    return json.dumps(dicts)

def deserialize(data,plot=False):
    # input is an array of dictionaries
    dicts = json.loads(data)
    V = len(dicts)
    
    nodeMap = {}

    # creating nodes and idx to node mapping
    nodes = set()
    for d in dicts:
        node = GraphNode(d['val'])
        nodeMap[d['idx']] = node
        nodes.add(node)

    #print('nodeMap = '+str(nodeMap))

    # node to location map
    locMap = node2locMap(nodes,nodeMap)

    # adding neighbors
    for d in dicts:
        node = nodeMap[d['idx']]
        for idxNgb in d['idxNgbs']:
            node.ngbs.add(nodeMap[idxNgb])

    if plot:
        visualize(nodes,locMap)

    return nodes

def node2locMap(nodes,nodeMap=None):
    if nodeMap == None:
        # idx to node map
        nodeMap = {}
        for idx,node in enumerate(nodes):
            nodeMap[idx] = node

    locMap = {}
    for idx in nodeMap.keys():
        #locMap[nodeMap[idx]] = (np.cos(idx/V*np.pi*2),np.sin(idx/V*np.pi*2))
        locMap[nodeMap[idx]] = (5*idx/V,np.sin(5*idx/V*np.pi*2))

    #print('locMap = '+str(locMap))

    return locMap

def visualize(nodes,locMap=None):
    if locMap == None:
        locMap = node2locMap(nodes)

    plt.figure()
    for node in nodes:
        loc = locMap[node]
        plt.scatter(loc[0],loc[1],lw=32)
        plt.annotate(str(node.val),xy=loc,xytext=(loc[0]+.1,loc[1]+.1),fontsize=15)
        for ngb in node.ngbs:
            locNgb = locMap[ngb]
            #plt.arrow(loc[0],loc[1],locNgb[0]-loc[0],locNgb[1]-loc[1],head_width=.1,head_length=.1,fc='k',ec='k')
            add_arrow(plt.plot([loc[0],locNgb[0]],[loc[1],locNgb[1]])[0])

    #plt.axis([-1.2,1.2,-1.2,1.2])
    axes = plt.axes()
    #axes.add_artist(plt.Circle((0, 0), 1.,color='k',ls='--',fill=False))
    axes.relim()
    axes.autoscale_view(False,True,True)
    plt.show()
    return

def add_arrow(line,size=20,color=None):
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()
    if xdata[-1]-xdata[0] >= 0:
        xStart = np.percentile(xdata,55)
        xEnd = np.percentile(xdata,45)
    else:
        xStart = np.percentile(xdata,45)
        xEnd = np.percentile(xdata,55)
    if ydata[-1]-ydata[0] >= 0:
        yStart = np.percentile(ydata,55)
        yEnd = np.percentile(ydata,45)
    else:
        yStart = np.percentile(ydata,45)
        yEnd = np.percentile(ydata,55)
    
    line.axes.annotate('',
        xytext=(xEnd,yEnd),
        xy=(xStart,yStart),
        arrowprops=dict(arrowstyle='-|>',color=color),
        size=size
    )
