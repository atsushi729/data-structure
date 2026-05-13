import unittest
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delete_node(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.delete_node(root.left, key)

        elif key > root.val:
            root.right = self.delete_node(root.right, key)

        else:
            # Case 1: no left child
            if not root.left:
                return root.right

            # Case 2: no right child
            if not root.right:
                return root.left

            # Case 3: two children
            successor = self.find_min(root.right)
            root.val = successor.val
            root.right = self.delete_node(root.right, successor.val)

        return root

    def find_min(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    def delete_node_v2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.delete_node_v2(root.left, key)
        elif key > root.val:
            root.right = self.delete_node_v2(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            node = root.right
            while node.left:
                node = node.left
            root.val = node.val
            root.right = self.delete_node_v2(root.right, node.val)
        return root


def tree_to_list(root):
    """Convert binary tree to level-order list."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

        # Tree:
        #         5
        #       /   \
        #      3     6
        #     / \     \
        #    2   4     7
        cls.root = TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(2),
                TreeNode(4)
            ),
            TreeNode(
                6,
                None,
                TreeNode(7)
            )
        )

        cls.test_cases = [
            (
                "Empty Tree",
                None,
                0,
                []
            ),
            (
                "Delete Leaf Node",
                TreeNode(
                    5,
                    TreeNode(
                        3,
                        TreeNode(2),
                        TreeNode(4)
                    ),
                    TreeNode(
                        6,
                        None,
                        TreeNode(7)
                    )
                ),
                2,
                [5, 3, 6, None, 4, None, 7]
            ),
            (
                "Delete Node With One Child",
                TreeNode(
                    5,
                    TreeNode(
                        3,
                        TreeNode(2),
                        TreeNode(4)
                    ),
                    TreeNode(
                        6,
                        None,
                        TreeNode(7)
                    )
                ),
                6,
                [5, 3, 7, 2, 4]
            ),
            (
                "Delete Node With Two Children",
                TreeNode(
                    5,
                    TreeNode(
                        3,
                        TreeNode(2),
                        TreeNode(4)
                    ),
                    TreeNode(
                        6,
                        None,
                        TreeNode(7)
                    )
                ),
                3,
                [5, 4, 6, 2, None, None, 7]
            ),
            (
                "Delete Root Node",
                TreeNode(
                    5,
                    TreeNode(
                        3,
                        TreeNode(2),
                        TreeNode(4)
                    ),
                    TreeNode(
                        6,
                        None,
                        TreeNode(7)
                    )
                ),
                5,
                [6, 3, 7, 2, 4]
            ),
            (
                "Delete Non-Existing Node",
                TreeNode(
                    5,
                    TreeNode(
                        3,
                        TreeNode(2),
                        TreeNode(4)
                    ),
                    TreeNode(
                        6,
                        None,
                        TreeNode(7)
                    )
                ),
                100,
                [5, 3, 6, 2, 4, None, 7]
            ),
            (
                "Single Node Tree",
                TreeNode(1),
                1,
                []
            ),
        ]

    def test_delete_node(self):
        for name, root, key, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.solution.delete_node(root, key)
                self.assertEqual(tree_to_list(result), expected)

    def test_delete_node_v2(self):
        for name, root, key, expected in self.test_cases:
            with self.subTest(name=name):
                result = self.solution.delete_node_v2(root, key)
                self.assertEqual(tree_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
