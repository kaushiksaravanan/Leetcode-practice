# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        k=-999
        if root:
            k=root.val
        def check(root):
            if root:
                if root.left and root.right:
                    if root.left.val<root.val<root.right.val:
                        return True
                    else:
                        return False
                elif root.left:
                    if root.left.val<root.val:
                        return True
                    else:
                        return False
                elif root.right:
                    if root.right.val>root.val:
                        return True
                    else:
                        return False
                if check(root.left) and check(root.right):
                    return True
                return False
            return False
        if not root.left and not root.right:
            return True 
        def check_left(root,val):
            if root:
                if root.val<val:
                        return check_left(root.left,val) and check_left(root.right,val)
                else:
                    return False
            return True

        def check_right(root,val):
            if root:
                # print(root.val,val,'--right')
                if root.val>val:
                        return check_right(root.left,val) and check_right(root.right,val)
                else:
                    return False
            return True

        val=root.val
        print(val)
        # print(check_right(root,val))
        print(check_left(root.left,val))
        print(check_right(root.right,val))

        def ino(root):
            if root:
                val=root.val
                print(root.val,val)

                if check_left(root.left,val) and check_right(root.right,val):
                    return ino(root.left) and ino(root.right)
                else:
                    return False
            return True
        
            

        return check(root) and ino(root)
