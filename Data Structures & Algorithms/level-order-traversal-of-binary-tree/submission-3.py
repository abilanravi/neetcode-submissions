# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = deque()
        queue.append(root)

        if not root:
            return []

        while queue:

            levelSize = len(queue)
            current_level = []

            while levelSize != 0:

                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                levelSize -= 1

            res.append(current_level)

        return res



        