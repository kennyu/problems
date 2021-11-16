from typing import List

class Trie:
    def __init__(self):
        self.end = False
        self.neighbors = [None]*26

    def insert(self, word: str) -> None:
        if word:
            letter = word[0]
            val = ord(letter)-97
            if not self.neighbors[val]:
                letter = Trie()
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

    def findNode(self, word: str) -> "Trie":
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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        columns = len(board)
        rows = len(board[0])
        board_words = set()
        def helper(i,j,visited_set, word):
            nonlocal board_words
            letter = board[i][j]
            new_word = word + letter
            if root.search(new_word):
                board_words.add(new_word)
                root.delete(new_word)
            if root.startsWith(new_word):
                candidates = []
                # left
                if i - 1 >= 0:
                    candidates.append((i-1,j))
                # right
                if i + 1 < columns:
                    candidates.append((i+1,j))
                # up
                if j - 1 >= 0:
                    candidates.append((i,j-1))
                # down
                if j + 1 < rows:
                    candidates.append((i, j+1))
                for c in candidates:
                    if c not in visited_set:
                        visited_set.add(c)
                        helper(*c, visited_set, new_word)
                        visited_set.remove(c)

        for word in words:
            root.insert(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited_set = set()
                visited_set.add((i,j))
                helper(i,j, visited_set, "")
        return list(board_words)

t = Trie()
t.insert("hello")
t.insert("helloworld")
t.delete("hello")
t.printAll(t)
t.delete("helloworld")
t.printAll(t)

s = Solution()
t1_board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
t1_words = ["oath","pea","eat","rain"]
assert set(s.findWords(t1_board, t1_words)) == set(["eat","oath"])
t2_board = [["a","b"],["c","d"]]
t2_words = ["abcb"]
assert set(s.findWords(t2_board, t2_words)) == set([])
t3_board = [["a","a"]]
t3_words = ["aaa"]
assert set(s.findWords(t3_board, t3_words)) == set([])
t4_board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
t4_words = ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]
assert set(s.findWords(t4_board, t4_words)) == set(["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"])
