from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        return_arr = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                return_arr[anagram_dict[sorted_word]].append(word)
            else:
                anagram_dict[sorted_word] = len(return_arr)
                return_arr.append([word])
        return return_arr
# Test Cases
l1 = ["eat","tea","tan","ate","nat","bat"]

s = Solution()
assert s.groupAnagrams(l1) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]