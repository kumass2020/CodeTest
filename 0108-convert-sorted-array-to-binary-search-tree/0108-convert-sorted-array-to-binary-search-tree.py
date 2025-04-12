# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        mid = (len(nums) - 1) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


        
        # N = len(nums)
        # mid = N // 2
        # def traverse(parent, lst):
        #     idx = (len(lst) - 1) // 2
        #     # print(lst, idx)
        #     if not lst:
        #         return
        #     new = TreeNode(lst[idx])
        #     if lst[idx] < parent.val:
        #         parent.left = new
        #     else:
        #         parent.right = new
        #     left_lst = lst[:idx]
        #     right_lst = lst[idx+1:]
        #     parent = new
        #     if left_lst:
        #         traverse(parent, left_lst)
        #     if right_lst:
        #         traverse(parent, right_lst)

        # root = TreeNode(nums[mid])
        # traverse(root, nums[:mid])
        # traverse(root, nums[mid+1:])
        # return root



            
