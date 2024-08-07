'''
1038. Binary Search Tree to Greater Sum Tree

that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.

'''


# Brute Force -> O(N*N)

class Solution:
    def inorder(self, root, ans):
        if root is None:
            return
        self.inorder(root.left, ans)
        ans.append(root.val)
        self.inorder(root.right, ans)

    def replace_value(self, root, inorder):
        if root is None:
            return

        self.replace_value(root.left, inorder)
        self.replace_value(root.right, inorder)

        node_sum = 0
        for i in inorder:
            if i > root.val:
                node_sum+=i

        root.val += node_sum

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        inorder = []
        
        self.inorder(root, inorder)

        self.replace_value(root, inorder)

        return root

        

# Optimal -> O(N)

class Solution:
    def inorder(self, root, ans):
        if root is None:
            return
        self.inorder(root.right, ans)
        ans[0] += root.val
        root.val = ans[0]
        self.inorder(root.left, ans)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        inorder = [0]
        
        self.inorder(root, inorder)

        return root
