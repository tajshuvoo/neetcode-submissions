class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s=[]
        for i in range(len(asteroids)):

            if len(s)==0:
                s.append(asteroids[i])
            else:
                last=s[-1]

                if last>0 and asteroids[i]<0:
                    if abs(last)>abs(asteroids[i]):
                        continue
                    
                    elif abs(last)==abs(asteroids[i]):
                        s.pop()

                    else:
                        s.pop()
                        s.append(asteroids[i])

                elif last<0 and asteroids[i]>0:

                    if abs(last)>abs(asteroids[i]):
                        continue
                        
                    elif abs(last)==abs(asteroids[i]):
                        s.pop()

                    else:
                        s.pop()
                        s.append(asteroids[i])
                else:
                    s.append(asteroids[i])
        
        return s
