class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()

        lcs = 1
        cs = 1 # longest consecutive subsequent
        for i in range(1,len(nums)):
            num = nums[i]
            if (num == nums[i-1]):
                continue
            elif (num == nums[i-1] + 1):
                cs += 1
            else:
                cs = 1
            if lcs < cs:
                lcs = cs
        return lcs



        