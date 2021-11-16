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

    def delete(self, word:str) -> bool:
        if self.search(word) is False:
            return False
        def delete_helper(node, word, count):
            has_another_word = node.end or node.neighbors.count(None) < 25
            if word:
                letter = word[0]
                val = ord(letter)-97
            if len(word) == 0:
                node.end = False
                return node.neighbors.count(None) != 26
            else:
                has_depth_word = delete_helper(node.neighbors[val], word[1:], count+1)
                if has_depth_word is False and has_another_word is True:
                    node.neighbors[val] = None
                    return True
                return has_another_word or has_depth_word if count != 0 else has_depth_word
        val = delete_helper(self, word, 0)
        if val is False:
            letter = word[0]
            val = ord(letter)-97
            self.neighbors[val] = None

    def printAll(self, root):
        queue = [("", root)]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            word, node = queue.pop(0)
            if node is not None:
                for nextLetter, nextNode in zip(alphabet, node.neighbors):
                    queue.append((word + nextLetter, nextNode))
                if node.end:
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
# -----------
assert obj.search("hello") is True
assert obj.search("hell") is False
assert obj.search("bob") is False
# -----------
assert obj.startsWith("hell") is True
assert obj.startsWith("bob") is False
# -----------
# Delete word between short and longer word
obj.insert("helloworld")
obj.insert("hell")
# print('before')
obj.printAll(obj)
# print('deleting...', "hello")
obj.delete("hello")
# print('after')
assert obj.search("hello") is False
assert obj.search("helloworld") is True
assert obj.search("hell") is True
# Delete shorter word in a longer word chain
obj.delete("hell")
assert obj.search("helloworld") is True
assert obj.search("hell") is False
# Delete only word
obj.insert("bobalice")
obj.delete("bobalice")
print('--------------')
obj.printAll(obj)
assert obj.startsWith("bob") is False
