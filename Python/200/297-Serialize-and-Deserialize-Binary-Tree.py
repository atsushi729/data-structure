import unittest
from typing import Optional
from collections import deque


#################### Solution ####################
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    def serialize_v2(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        serialized_values = []

        def preorder_traversal(node: Optional[TreeNode]):
            if node is None:
                serialized_values.append("N")
                return
            serialized_values.append(str(node.val))
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        preorder_traversal(root)
        return ",".join(serialized_values)

    def deserialize_v2(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(","))

        def build_tree() -> Optional[TreeNode]:
            try:
                val = next(values)
            except StopIteration:
                return None

            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()

    def serialize_v3(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "N"
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

    def deserialize_v3(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == "N":
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if values[i] != "N":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1

        return root


#################### Test Case ####################
class TestCodec(unittest.TestCase):
    def test_serialize(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        codec = Codec()
        self.assertEqual(codec.serialize(root), "1,2,N,N,3,4,N,N,5,N,N")

    def test_deserialize(self):
        data = "1,2,N,N,3,4,N,N,5,N,N"
        codec = Codec()
        root = codec.deserialize(data)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.right.left.val, 4)
        self.assertEqual(root.right.right.val, 5)

    def test_serialize_v2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        codec = Codec()
        self.assertEqual(codec.serialize_v2(root), "1,2,N,N,3,4,N,N,5,N,N")

    def test_deserialize_v2(self):
        data = "1,2,N,N,3,4,N,N,5,N,N"
        codec = Codec()
        root = codec.deserialize_v2(data)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.right.left.val, 4)
        self.assertEqual(root.right.right.val, 5)

    def test_serialize_v3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        codec = Codec()
        self.assertEqual(codec.serialize_v3(root), "1,2,3,N,N,4,5,N,N,N,N")

    def test_deserialize_v3(self):
        data = "1,2,3,N,N,4,5,N,N,N,N,N"
        codec = Codec()
        root = codec.deserialize_v3(data)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.right.left.val, 4)
        self.assertEqual(root.right.right.val, 5)
