"""
# Definition for a Node.
"""

from typing import Optional
import unittest


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


class TestSolution(unittest.TestCase):
    def test_cloneGraph(self):
        solution = Solution()

        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        copy1 = solution.cloneGraph(node1)
        self.assertEqual(copy1.val, 1)
        self.assertEqual(copy1.neighbors[0].val, 2)
        self.assertEqual(copy1.neighbors[1].val, 4)
        self.assertEqual(copy1.neighbors[0].neighbors[0].val, 1)
        self.assertEqual(copy1.neighbors[0].neighbors[1].val, 3)
        self.assertEqual(copy1.neighbors[1].neighbors[0].val, 1)
        self.assertEqual(copy1.neighbors[1].neighbors[1].val, 3)
