class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26

        for x in s:
            arr[ord(x) - ord('a')] += 1
        
        for x in t:
            arr[ord(x) - ord('a')] -= 1

        for x in arr:
            if x != 0:
                return False
        return True
        


        