class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1] * len(nums)
        post_prod = [1] * len(nums)

        for i in range(1,len(nums)):
            pre_prod[i] = pre_prod[i-1]*nums[i-1]

        for j in range(-2,-len(nums)-1,-1):
            post_prod[j] = post_prod[j+1] *nums[j+1]

        output=[0] * len(nums)

        for k in range(len(nums)):
            output[k] = pre_prod[k] *post_prod[k]
        
        return output


