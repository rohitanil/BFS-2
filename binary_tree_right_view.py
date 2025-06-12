# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Time Complexity: O(N) where N is number of nodes in binary tree
Space Complexity: O(N) for the queue.
We do a level order traversal of binary tree using BFS. At each level, we check if its the first time we are reaching that level or not
If its first time, length of result and level will match. If its not matching, it means some other node from that level was
visited before and hence that should be the right side element.

Traversal flow-> first to the right size and then to the left side for right side view.
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def bfs(node, level):
            queue = [(node, level)]
            while queue:
                elem = queue.pop(0)
                curr_node = elem[0]
                curr_level = elem[1]
                size = len(result)
                if size == curr_level:
                    result.append(curr_node.val)
                if curr_node.right:
                    queue.append((curr_node.right, curr_level + 1))
                if curr_node.left:
                    queue.append((curr_node.left, curr_level + 1))

        if root == None:
            return result
        bfs(root, 0)
        return result