"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.clones = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node in self.clones:
            return self.clones[node]
        copy = Node(node.val)
        self.clones[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(self.cloneGraph(n))
        return copy