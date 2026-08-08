import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1
        
        ans = []
        for key,val in num_map.items():
            heapq.heappush(ans,(val,key))
            if len(ans) > k:
                heapq.heappop(ans)

        return [key for val,key in ans]

        