class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]

        for i in range(len(tokens)):
            
            if tokens[i].lstrip('-').isdigit():
                s.append(int(tokens[i]))

            else:
                last=s.pop()
                first=s.pop()

                if tokens[i]=='+':
                    s.append(first+last)
                elif tokens[i]=='-':
                    s.append(first-last)   
                elif tokens[i]=='*':
                    s.append(first*last)
                elif tokens[i]=='/':
                    s.append(first//last)

        return s.pop()