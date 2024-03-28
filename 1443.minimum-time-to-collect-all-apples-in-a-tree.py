#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
from typing import List

class node:
    def __init__(self, value, hasApple=False, children=[]):
        self.value = value
        self.hasApple = hasApple
        self.children = children

def buildTree(edges: List[List[int]], hasApple: List[bool], value) -> node:
    children = []
    # we could speed this up by removing edges that arent part of this subtree
    i = 0
    while i < len(edges):
        edge = edges[i]
        if edge[0] == value:
            edges.remove(edge)
            children.append(buildTree(edges, hasApple, edge[1]))
        # edges can apparently be written either direction
        elif edge[1] == value:
            edges.remove(edge)
            children.append(buildTree(edges, hasApple, edge[0]))
        else:
            i += 1
    head = node(value, hasApple[value], children)
    return head

# find leaf nodes, if apple add +2 to the time count
def pickApples(currNode: node) -> int:
    timePicking = 0
    index = currNode.value
    for n in currNode.children:
        timePicking += pickApples(n)
    
    # count this node if we either have an apple here or picked one downstream
    if currNode.value != 0:
        if timePicking > 0 or currNode.hasApple:
            timePicking += 2
    return timePicking

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = buildTree(edges, hasApple, 0)
        timePicking = pickApples(tree)
        return timePicking

# if __name__ == '__main__':
#     n = 7
#     edges = [[0,1],[1,2],[2,3],[1,4],[2,5],[2,6],[4,7]]
#     hasApple = [True,True,False,True,False,True,True,False]
#     Solution.minTime(None, n, edges, hasApple)

# @lc code=end

