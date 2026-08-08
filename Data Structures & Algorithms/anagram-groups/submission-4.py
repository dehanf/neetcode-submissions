class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_arr = [''.join(sorted(s)) for s in strs]
        num_occ = {} # number occurences
        for i,s in enumerate(sorted_arr):
            if s in num_occ:
                num_occ[s].append(i)
            else:
                num_occ[s] =[i]
        final = []
        for key,val in num_occ.items():
            final.append([strs[i] for i in val])
        return final
                    
                



        