class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash_map = {"5": 0, "10": 0, "20": 0}
        for b in bills:
            if b == 5:
                hash_map["5"] += 1
            if b == 10:
                if hash_map["5"] > 0:
                    hash_map["5"] -= 1
                    hash_map["10"] += 1
                else:
                    return False
            if b == 20:
                if hash_map["10"] > 0:
                    if hash_map["5"] > 0:
                        hash_map["5"] -= 1
                        hash_map["10"] -= 1
                        hash_map["20"] += 1
                    else:
                        return False
                else:
                    if hash_map["5"] >= 3:
                        hash_map["5"] -= 3
                        hash_map["20"] += 1
                    else:
                        return False
        return True