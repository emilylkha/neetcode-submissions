class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # put it into some representation to easily check
        anagrams = defaultdict(list) # k = representation, v = word
        for word in strs:
            rep = [0] * 26
            for letter in word:
                rep[ord(letter) - ord('a')] += 1
            anagrams[str(rep)].append(word)
        return list(anagrams.values())