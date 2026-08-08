
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            adj = target - nums[i] #value to search
            if adj in num_dict:
                return [num_dict[adj],i]
            num_dict[nums[i]] = i
            
        
            




        