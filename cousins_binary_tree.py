# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Time Complexity -> O(N)
Space Complexity -> O(N) since using deque

Logic
We do level order traversal, so use the length of the queue to achieve that.
1. At each node, if we have child nodes, check if left child and right child have x and y values. If yes,
It means they are not cousins but siblings. Return a False

2. If the above condition isnt met, it means the values we are looking for are not siblings and will belong to different
parents in case they exist in the binary tree.

2.1 Check if left child exists, if yes, check if the value equals x or y and update the level in the corresponding level flags
2.2 Check if right child exists, if yes, check if value equals x or y and update the level in the corresponding level flags

At the end return True if levels of x and y are equal.
"""
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def bfs(node, lvl):
            queue = deque([(node, lvl)])
            found_x = found_y = -1
            while queue:
                size = len(queue)
                for _ in range(size):
                    elem = queue.popleft()
                    curr = elem[0]
                    curr_level = elem[1]
                    if curr.left and curr.right:
                        if curr.left.val == x and curr.right.val == y or curr.left.val == y and curr.right.val == x:
                            return False
                    next_level = curr_level + 1
                    if curr.left:
                        if curr.left.val == x:
                            found_x = next_level
                        if curr.left.val == y:
                            found_y = next_level
                        queue.append((curr.left, next_level))
                    if curr.right:
                        if curr.right.val == x:
                            found_x = next_level
                        if curr.right.val == y:
                            found_y = next_level
                        queue.append((curr.right, next_level))
            return found_x == found_y

        return bfs(root, 0)
