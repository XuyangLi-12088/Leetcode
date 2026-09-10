class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            key = key
            val = self.hash_map[key]
            del self.hash_map[key]
            self.hash_map[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]
            self.hash_map[key] = value
        else:
            if self.cap > len(self.hash_map):
                self.hash_map[key] = value
            else:
                first_key = next(iter(self.hash_map))
                del self.hash_map[first_key]
                self.hash_map[key] = value

        return




            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)