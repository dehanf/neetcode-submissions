class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = dict()
        for i in range(len(nums)):
            other = target - nums[i]
            if other not in num_map:
                num_map[nums[i]] = i 
            else:
                return[num_map[other],i]


        