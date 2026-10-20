from typing import Optional
import unittest

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]

            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

    def clone_graph_v2(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        q = [node]
        oldToNew[node] = Node(node.val)

        while q:
            cur = q.pop(0)
            for nei in cur.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[cur].neighbors.append(oldToNew[nei])

        return oldToNew[node]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.implementations = [
            self.solution.cloneGraph,
            self.solution.clone_graph_v2,
        ]

    def build_graph(self, adj_list):
        if not adj_list:
            return None

        nodes = [Node(i + 1) for i in range(len(adj_list))]

        for i, neighbors in enumerate(adj_list):
            nodes[i].neighbors = [
                nodes[j - 1] for j in neighbors
            ]

        return nodes[0]

    def assert_deep_copy(self, original, cloned):
        if original is None:
            self.assertIsNone(cloned)
            return

        visited = set()
        stack = [(original, cloned)]

        while stack:
            old, new = stack.pop()

            if old in visited:
                continue

            visited.add(old)

            # Different objects
            self.assertIsNot(old, new)

            # Same values and structure
            self.assertEqual(old.val, new.val)
            self.assertEqual(
                len(old.neighbors),
                len(new.neighbors)
            )

            for old_nei, new_nei in zip(
                    old.neighbors, new.neighbors
            ):
                self.assertEqual(old_nei.val, new_nei.val)
                self.assertIsNot(old_nei, new_nei)
                stack.append((old_nei, new_nei))

    def test_clone_graph(self):
        test_cases = [
            # Empty graph
            [],

            # Single node
            [[]],

            # Two connected nodes
            [[2], [1]],

            # Four nodes with cycle
            [[2, 4], [1, 3], [2, 4], [1, 3]],

            # Triangle
            [[2, 3], [1, 3], [1, 2]],

            # Linear graph
            [[2], [1, 3], [2, 4], [3]],

            # Self-loop
            [[1]],
        ]

        for impl in self.implementations:
            for adj_list in test_cases:
                with self.subTest(
                        impl=impl.__name__,
                        adj_list=adj_list
                ):
                    original = self.build_graph(adj_list)
                    cloned = impl(original)

                    self.assert_deep_copy(original, cloned)

    def test_independent_copy(self):
        for impl in self.implementations:
            with self.subTest(impl=impl.__name__):
                original = self.build_graph([[2], [1]])
                cloned = impl(original)

                cloned.val = 100
                cloned.neighbors[0].val = 200

                self.assertEqual(original.val, 1)
                self.assertEqual(original.neighbors[0].val, 2)


if __name__ == "__main__":
    unittest.main()
