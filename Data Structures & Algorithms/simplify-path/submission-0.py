class Solution:
    def simplifyPath(self, path: str) -> str:
        part = path.split("/")
        s=[]

        for p in part:
            if p=="" or p==".":
                continue
            elif p=="..":
                if s:
                    s.pop()
            else:
                s.append(p)

        return "/"+"/".join(s)