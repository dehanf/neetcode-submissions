class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        if len(strs) == 0:
            return ""
        for s in strs:
            string += str(len(s))
            string += '#'
            string += s
            
        return string


    def decode(self, s: str) -> List[str]:
        strs = []
        idx_string = 0 
        while idx_string < len(s):
            num_end = idx_string
            while s[num_end] != '#': #get the number length
                num_end += 1

            num = int(s[idx_string : num_end]) # get the number
            idx_string = num_end +1 # skip the hash
            word = s[idx_string:idx_string+num] # get the word
            strs.append(word)
            idx_string += num
            
            
        return strs




