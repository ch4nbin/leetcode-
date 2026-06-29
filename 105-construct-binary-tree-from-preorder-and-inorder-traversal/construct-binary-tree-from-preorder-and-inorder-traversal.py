# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # so basically preorder is you go root first and then left
        # subtree then right and in order is left, root, mid so,
        # you use preorder whos first value is the root and find it
        # in the inorder array and its the midpoint because everything
        # to the left is left subtree and everything to the right is
        # right subtree and then to build left and right from a given node
        # you recurse down with the resepctive direction subtrees slice
        # of preorder and inorder and if theyre ever empty you know youve done all the work
        if not preorder or not inorder:
            return None
        
        # root is always first val in preorder
        cur_root = TreeNode(preorder[0])
        
        # split between subtrees is root in inorder
        mid = inorder.index(preorder[0])

        cur_root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        cur_root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return cur_root