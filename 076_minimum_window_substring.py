import copy, collections

class Solution:
    def minWindowSliding(self, s: str, t: str) -> str:
        scounts = dict()
        tcounts = dict()
        # for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        #     scounts[letter] = 0
            # tcounts[letter] = 0

        for letter in t:
            if letter not in tcounts:
                tcounts[letter] = 0
            tcounts[letter] += 1

        l = 0
        r = 0

        while r < len(s):
            letter = s[r]
            if letter not in scounts:
                scounts[letter] = 0
            scounts[letter] += 1

            matching = True
            for k, v in tcounts.items():
                if k not in scounts or v > scounts[k]:
                    matching = False
                    break

            if matching:
                print("found a match", s[l:r+1])
                while l < r:
                    left_letter = s[l]
                    if left_letter in tcounts:
                        print(left_letter, scounts[left_letter], tcounts[left_letter])
                        if scounts[left_letter] > tcounts[left_letter]:
                            scounts[left_letter] -= 1
                        else:
                            break
                    l += 1
                print("shortened match", s[l:r+1])
                l = r
                scounts = dict()
                scounts[s[l]] = 1

            r += 1

    def minWindow(self, s: str, t: str) -> str:
        # t_count = dict()
        # for letter in t:
        #     if letter in t_count:
        #         t_count[letter] = 1
        #     else:
        #         t_count[letter] += 1
        # l = 0
        # r = l
        # need = copy.deepcopy(t_count)
        # for idx, letter in enumerate(s):
        #     if letter in need and need[letter] > 0:
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            print("-----------------------------------")
            print("missing ", missing, "need ", need)
            missing -= need[c] > 0
            need[c] -= 1
            print("missing ", missing, "need ", need)
            print("-----------------------------------")
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

s = Solution()

print(s.minWindow("ADOBECODEBANC", "ABC"))
assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"

#The current window is s[i:j] and the result window is s[I:J].
#In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing.
#In the loop, first add the new character to the window.
#Then, if nothing is missing, remove as much as possible from the window start and then update the result
