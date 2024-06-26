'''
1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root, ans):
        if root is None:
            return

        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

    def constructbst(self, arr):
        if len(arr) == 0:
            return None
        
        mid = len(arr)//2
        root = TreeNode(arr[mid])
        root.left = self.constructbst(arr[:mid])
        root.right = self.constructbst(arr[mid+1:])
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        self.inorder(root, ans)

        newroot = self.constructbst(ans)

        return newroot


        