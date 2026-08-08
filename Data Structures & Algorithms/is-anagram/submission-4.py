class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        arr = [0] * 26

        for x,y in zip(s,t):
            arr[ord(x) - ord('a')] += 1
            arr[ord(y) - ord('a')] -= 1
        
        return all(x==0 for x in arr)
        


        