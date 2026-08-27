class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_dict = {'(' : ')','{':'}','[':']'}
        if not s:
            return False


        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif stack and (i == s_dict[stack[-1]]) :
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
        