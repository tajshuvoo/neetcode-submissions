class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch==']':

                my_str=""
                while stack[-1]!='[':
                    my_str=stack.pop()+my_str
                stack.pop()

                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                num=int(num)

                stack.append(my_str*num)
            
            else:
                stack.append(ch)


        return "".join(stack)