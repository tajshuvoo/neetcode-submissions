class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch==']':

                my_str=""
                while stack[-1]!='[':
                    my_str+=stack.pop()
                my_str=my_str[::-1]
                stack.pop()

                num=""
                while stack and stack[-1].isdigit():
                    num+=stack.pop()
                num=int(num[::-1])

                stack.append(my_str*num)
            
            else:
                stack.append(ch)


        return "".join(stack)