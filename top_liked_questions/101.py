class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def check(root1, root2):
            
            if not root1 and root2: return False
            if not root2 and root1: return False
            if not root1 and not root2: return True
            
            if root1.val == root2.val:
                return check(root1.left, root2.right) and check(root1.right, root2.left)
            else:
                return False
            
        if root:
            return check(root.left, root.right)
        return True
