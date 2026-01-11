# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return 0, None
            
            l_depth, l_lca = dfs(node.left)
            r_depth, r_lca = dfs(node.right)
            
            if l_depth > r_depth:
                return l_depth + 1, l_lca
            
            elif r_depth > l_depth:
                return r_depth + 1, r_lca
            
            # else, this node LCA
            else:
                return l_depth + 1, node
                
        return dfs(root)[1]