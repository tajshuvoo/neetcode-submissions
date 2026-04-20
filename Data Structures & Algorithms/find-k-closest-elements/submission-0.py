class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        data=[[0]*len(arr) for _ in range(2)]

        for i in range(len(arr)):
            data[1][i]=i
            data[0][i]=abs(arr[i]-x)
        
        idx=sorted(range(len(data[0])), key= lambda i: data[0][i])
        sorted_data= [[row[i] for i in idx ]for row in data]

        sorted_data=sorted_data[1][:k]

        res=[]
        for i in sorted_data:
            res.append(arr[i])
        res=sorted(res)
        return res