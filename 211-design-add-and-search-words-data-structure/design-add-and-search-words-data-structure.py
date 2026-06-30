class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        return   

    def search(self, word: str) -> bool:
        # BFS
        queue = deque([(0, self.root)])
        while queue:
            i, node = queue.popleft()
            if i == len(word):
                if node.is_end_of_word:
                    return True
                continue
            if word[i] == ".":
                for child in node.children:
                    queue.append((i + 1, node.children[child]))
            else:
                if word[i] in node.children:
                    queue.append((i + 1, node.children[word[i]]))

        return False 


    # def search(self, word: str) -> bool:
    #     def dfs(node, index):
    #         if index == len(word):
    #             return node.is_end_of_word

    #         if word[index] == ".":
    #             for child in node.children.values():
    #                 if dfs(child, index+1):
    #                     return True

    #         if word[index] in node.children:
    #             return dfs(node.children[word[index]], index+1)

    #         return False

    #     return dfs(self.root, 0)


    

            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)