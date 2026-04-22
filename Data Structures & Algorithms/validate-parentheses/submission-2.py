class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for brac in s:

            if brac =='[' or brac =='{' or brac == '(':
                stack.append(brac)
            
            else:
                if len(stack)==0:
                    return False

                last=stack[-1]
                if last=='(' and brac==')':
                    stack.pop()
                elif last=='{' and brac=='}':
                    stack.pop()
                elif last=='[' and brac==']':
                    stack.pop()

        return len(stack)==0
