class TrieRecursive:
    def __init__(self):
        self.end = False
        self.neighbors = [None]*26

    def insert(self, word: str) -> None:
        if word:
            letter = word[0]
            val = ord(letter)-97
            if not self.neighbors[val]:
                letter = TrieRecursive()
                self.neighbors[val] = letter
            self.neighbors[val].insert(word[1:])
        else:
            self.end = True

    def search(self, word: str) -> bool:
        node = self.findNode(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.findNode(prefix)
        return node is not None

    def findNode(self, word: str) -> "TrieRecursive":
        if word:
            letter = word[0]
            val = ord(letter)-97
            if not self.neighbors[val]:
                return None
            else:
                return self.neighbors[val].findNode(word[1:])
        else:
            return self

    def printAll(self, root):
        queue = [("", root)]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            word, node = queue.pop(0)
            if node is not None:
                for nextLetter, nextNode in zip(alphabet, node.neighbors):
                    queue.append((word + nextLetter, nextNode))
                if node.end_of_word:
                    print("End of Word", word)

class TrieIterative:
    def __init__(self):
        self.end = False
        self.neighbors = [None]*26

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass

    def findNode(self, word: str) -> "TrieIterative":
        pass

    def printAll(self, root):
        pass

# Test Cases
obj = TrieRecursive()
obj.insert("hello")
obj.printAll(obj)
assert obj.search("hello") is True
assert obj.search("hell") is False
assert obj.search("bob") is False
assert obj.startsWith("hell") is True
assert obj.startsWith("bob") is False
