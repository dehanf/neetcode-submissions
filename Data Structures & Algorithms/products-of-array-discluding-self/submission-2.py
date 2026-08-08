class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##nums = [1,2,4,6]
        ans = [1] * len(nums)
        pre = 1
        post = 1
        
        for i in range(len(nums)):
            ans[i] = pre
            pre = nums[i] * pre
        
        for j in range(1,len(nums)+1):
            ans[-j] = ans[-j]* post
            post = post * nums[-j]
        return ans
            


        