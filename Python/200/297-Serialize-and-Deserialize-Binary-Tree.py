import unittest
from collections import deque


#################### Solution ####################
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
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
        values = []

        def preorder(node):
            if node is None:
                values.append("N")
                return

            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(values)

    def deserialize_v2(self, data):
        values = iter(data.split(","))

        def build():
            value = next(values)

            if value == "N":
                return None

            node = TreeNode(int(value))
            node.left = build()
            node.right = build()

            return node

        return build()

    def serialize_v3(self, root):
        if not root:
            return "N"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")

        return ",".join(result)

    def deserialize_v3(self, data):
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


#################### Test ####################

class TestCodec(unittest.TestCase):

    @classmethod
    def build_tree(cls, values):
        if not values:
            return None

        root = TreeNode(values[0])

        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            if index < len(values) and values[index] is not None:
                node.left = TreeNode(values[index])
                queue.append(node.left)

            index += 1

            if index < len(values) and values[index] is not None:
                node.right = TreeNode(values[index])
                queue.append(node.right)

            index += 1

        return root

    @classmethod
    def setUpClass(cls):
        cls.codec = Codec()

        cls.test_cases = [
            {
                "name": "empty tree",
                "root": None,
            },
            {
                "name": "single node",
                "root": TreeNode(1),
            },
            {
                "name": "balanced tree",
                "root": cls.build_tree(
                    [1, 2, 3, 4, 5]
                ),
            },
            {
                "name": "left skewed",
                "root": cls.build_tree(
                    [1, 2, None, 3, None, 4]
                ),
            },
            {
                "name": "right skewed",
                "root": cls.build_tree(
                    [1, None, 2, None, 3, None, 4]
                ),
            },
            {
                "name": "negative values",
                "root": cls.build_tree(
                    [-1, -2, -3]
                ),
            },
            {
                "name": "duplicate values",
                "root": cls.build_tree(
                    [1, 1, 1, 1, 1]
                ),
            },
            {
                "name": "large values",
                "root": cls.build_tree(
                    [1000000, 999999, 888888]
                ),
            },
            {
                "name": "mixed tree",
                "root": cls.build_tree(
                    [10, 5, 15, None, 8, 12, 20]
                ),
            },
        ]

    def test_serialize_deserialize(self):
        """
        serialize -> deserialize -> serialize
        """

        for case in self.test_cases:
            with self.subTest(case=case["name"]):
                serialized = self.codec.serialize(case["root"])
                restored = self.codec.deserialize(serialized)

                self.assertEqual(
                    serialized,
                    self.codec.serialize(restored)
                )

    def test_serialize_deserialize_v2(self):
        """
        serialize_v2 -> deserialize_v2 -> serialize_v2
        """

        for case in self.test_cases:
            with self.subTest(case=case["name"]):
                serialized = self.codec.serialize_v2(case["root"])
                restored = self.codec.deserialize_v2(serialized)

                self.assertEqual(
                    serialized,
                    self.codec.serialize_v2(restored)
                )

    def test_serialize_deserialize_v3(self):
        """
        serialize_v3 -> deserialize_v3 -> serialize_v3
        """

        for case in self.test_cases:
            with self.subTest(case=case["name"]):
                serialized = self.codec.serialize_v3(case["root"])
                restored = self.codec.deserialize_v3(serialized)

                self.assertEqual(
                    serialized,
                    self.codec.serialize_v3(restored)
                )


if __name__ == "__main__":
    unittest.main()
