class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list)

        

        for str_ in strs:
            alphabet = [0] * 26
            for s in str_:
                alphabet[ord(s)-ord('a')] += 1

            ##key = "".join([str(num) for num in alphabet])
            key = tuple(alphabet)

            """if(key in anagrams):
                anagrams[key].append(str_)
            else:
                anagrams[key] = [str_]"""
            anagrams[key].append(str_)
            
        return list(anagrams.values())