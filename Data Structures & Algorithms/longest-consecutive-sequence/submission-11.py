class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0
        num_set = set()
        for num in nums:
            num_set.add(num)
        cs = 1
        lcs = 1
        for num in num_set:
           
            if num-1 in num_set:
                continue
            else:
                next = num + 1
                while next in num_set:
                    cs += 1
                    next += 1
                    
                if lcs < cs:
                        lcs = cs
            cs = 1
        return lcs



        