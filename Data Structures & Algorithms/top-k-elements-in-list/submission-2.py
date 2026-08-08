from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_occ = defaultdict(int) #number occurences
        for num in nums:
            num_occ[num] += 1
        
        sorted_dict = dict(sorted(num_occ.items(),key = lambda x:x[1],reverse= True))
        final = []
        for key,_ in sorted_dict.items():
            if len(final) >= k:
                break
            final.append(key)
               
        return final
         