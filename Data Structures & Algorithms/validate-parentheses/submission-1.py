class Solution:
    def isValid(self, s: str) -> bool:

        closed = {")":"(","}":"{", "]":"["}
        stack = []


        for char in s:
            if char in closed:
                if stack and stack[-1] == closed[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False 



                






