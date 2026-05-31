class Solution:

    def encode(self, strs: List[str]) -> str:
        # how long the next string is then #
        return ''.join([str(len(s)) + '#' + s for s in strs])

    def decode(self, s: str) -> List[str]:
        start, end = 0, 0
        strs = []
        while start < len(s):
            # find len of next string
            while s[end] != '#':
                end += 1
            length = int(s[start:end])
            start = end + 1
            end = start + length
            strs.append(s[start:end])
            start = end
        return strs

