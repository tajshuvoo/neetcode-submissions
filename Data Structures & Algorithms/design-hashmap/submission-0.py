class MyHashMap:

    def __init__(self):
        self.data = [0]*10000

    def put(self, key: int, value: int) -> None:
        # if self.data[key] !=0:
        self.data[key] = value

    def get(self, key: int) -> int:
        if self.data[key] ==0:
            return -1
        return self.data[key]

    def remove(self, key: int) -> None:
        self.data[key] =0


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)