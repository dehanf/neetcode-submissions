class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = [] #final array to store results
        sorted_arr = [sorted(s) for s in strs ]
        for i in range(len(sorted_arr)):
            before = [strs[i]]
            if sorted_arr[i] == 0:
                    continue 
            for j in range(len(sorted_arr)):
                if sorted_arr[j] == 0:
                    continue 
                if sorted_arr[i] == sorted_arr[j] and i != j:
                    sorted_arr[j] = 0
                    before.append(strs[j])
            final.append(before)
            sorted_arr[i] = 0
        return final
                    
                    



        