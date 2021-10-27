class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        substring_window_len = 1
        longest_len = 1
        bag = {s[0]:0}
        for idx, letter in enumerate(s[1:],1):
            if letter in bag:
                last_idx_elem = bag.pop(letter)
                substring_window_len = (idx - last_idx_elem)
                keys_to_pop = [key for key, value in bag.items() if value < last_idx_elem]
                [ bag.pop(key) for key in keys_to_pop ]
            else:
                substring_window_len += 1
            bag[letter] = idx
            longest_len = max(longest_len, substring_window_len)
        return longest_len

# Test Cases
l1 = "abba"

s = Solution()
assert(s.lengthOfLongestSubstring(l1)==2)
