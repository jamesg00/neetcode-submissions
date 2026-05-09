class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        #initialize stack

        for tok in tokens:
            #iterate over our tokens

            if tok not in "/*-+":
                stack.append(int(tok))

                #if we dont have any tokens in we append ints of our token 
                #to stack
            
            else:
                #a = stack.pop and b = stack.pop to do multipication
                a = stack.pop()
                b = stack.pop()

                #convert them to ints when we do operaion
                if tok == "*":
                    stack.append(int(b*a))
                elif tok == "/":
                    #handle if intger is 0 (for b)
                    if b == 0:
                        stack.append(0)
                    else:
                        stack.append(int(b/a))
                elif tok == "-":
                    stack.append(int(b-a))
                elif tok == "+":
                    stack.append(int(b+a))
        #return stack[0]
        return stack[0]





              
       



        