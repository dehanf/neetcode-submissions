class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        sorted_nums = sorted(nums)
        output = []

        for i,num in enumerate(sorted_nums):
            if num > 0:
                break
            if i > 0 and sorted_nums[i-1] == num:
                continue
            left = i+1
            right = len(sorted_nums)-1

            while left < right :
                total = num + sorted_nums[left] + sorted_nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1
                else:
                    output.append([num,sorted_nums[left],sorted_nums[right]])
                    left += 1
                    right -= 1
               
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1

                
        return output



            