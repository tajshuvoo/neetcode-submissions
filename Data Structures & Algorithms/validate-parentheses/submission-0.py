class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for brac in s:

            if brac =='[' or brac =='{' or brac == '(':
                stack.append(brac)
            
            else:
                last=stack[-1]
                if last=='(' and brac==')':
                    stack.pop()
                elif last=='{' and brac=='}':
                    stack.pop()
                elif last=='[' and brac==']':
                    stack.pop()

        return len(stack)==0
