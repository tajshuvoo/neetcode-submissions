class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]

        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isdigit():
                s.append(int(tokens[i]))
            elif tokens[i]=='+':
                s.append(s.pop()+s.pop())
            elif tokens[i]=='-':
                s.append(s.pop()-s.pop())   
            elif tokens[i]=='*':
                s.append(s.pop()*s.pop())
            elif tokens[i]=='/':
                s.append(s.pop()/s.pop())

        return s.pop()