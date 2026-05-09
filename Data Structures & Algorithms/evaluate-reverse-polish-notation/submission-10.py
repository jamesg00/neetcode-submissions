class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:

            if tok not in "/*-+":
                stack.append(int(tok))
            
            else:
                a = stack.pop()
                b = stack.pop()


                if tok == "*":
                    stack.append(int(a*b))
                elif tok == "/":
                    if b == 0:
                        stack.append(0)
                    else:
                        stack.append(int(b/a))
                elif tok == "-":
                    stack.append(int(b-a))
                elif tok == "+":
                    stack.append(int(b+a))
        
        return stack[0]





              
       



        