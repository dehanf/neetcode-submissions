class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##nums = [1,2,4,6]
        pre = [1]
        post = [1] * len(nums)
        for i in range(len(nums)-1):
            pre.append(pre[i]*nums[i])
        
        for j in range(2,len(nums)+1):
            post[-j] = nums[len(nums)-j+1] * post[len(nums)-j+1]

        print(pre)

        print(post)


        return [pre[k]*post[k] for k in range(len(nums))]


        