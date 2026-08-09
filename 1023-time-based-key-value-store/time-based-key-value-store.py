class TimeMap:
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append([value, timestamp])
        else:
            self.timemap[key] = [[value, timestamp]]
        return

    def get(self, key: str, timestamp: int) -> str:
        # 找到self.timemap对应key的list
        if key not in self.timemap:
            return ""

        value_list = self.timemap[key]

        if timestamp < value_list[0][1]:
            return ""

        n = len(value_list)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if value_list[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # 如果timemap里有time == timestamp的元素
        if left < n and value_list[left][1] == timestamp:
            return value_list[left][0]
        # 如果timemap里没有time == timestamp的元素
            # 所有元素的time都小于timestamp
            # 所有元素的time都大于timestamp（开头检查了），直接return “”
            # 有元素的time小于timestamp，有元素的time大于timestamp
        return value_list[left - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)