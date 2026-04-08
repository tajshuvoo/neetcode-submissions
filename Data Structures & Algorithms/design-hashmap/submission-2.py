class MyHashMap:

    def __init__(self):
        self.data = {}

    def put(self, key: int, value: int) -> None:
        self.data[key] = value  # Assignment (=) is required to save

    def get(self, key: int) -> int:
        return self.data.get(key, -1) # Returns -1 if key is missing

    def remove(self, key: int) -> None:
        self.data.pop(key, None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)