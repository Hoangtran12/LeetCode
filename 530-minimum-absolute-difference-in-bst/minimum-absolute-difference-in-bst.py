# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.prev = float('inf')  # Variable to track the previous node value
        self.ans = float('inf')  # Variable to store the minimum absolute difference

    def getMinimumDifference(self, root):
        self.inOrder(root)  # Perform an inorder traversal of the binary tree
        return self.ans  # Return the minimum absolute difference

    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)  # Recursively traverse the left subtree

        self.ans = min(self.ans, abs(root.val - self.prev))  # Update the minimum absolute difference
        self.prev = root.val  # Update the previous node value

        if root.right:
            self.inOrder(root.right)  # Recursively traverse the right subtree
        