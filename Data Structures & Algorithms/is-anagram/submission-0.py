class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        for letter in s:
            if letter in countS:
                countS[letter] += 1
            else:
                countS[letter] = 1
        countT = {}
        for letter in t:
            if letter in countT:
                countT[letter] += 1
            else:
                countT[letter] = 1
        for letter in countS.keys():
            if letter not in countT or countS[letter] != countT[letter]:
                return False
        return True