from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_minimum_difference(self, root: Optional[TreeNode]) -> int:
        node_val_list = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            node_val_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        node_val_list.sort()
        min_diff = float("inf")

        for i in range(len(node_val_list) - 1):
            min_diff = min(min_diff, abs(node_val_list[i] - node_val_list[i + 1]))

        return min_diff
