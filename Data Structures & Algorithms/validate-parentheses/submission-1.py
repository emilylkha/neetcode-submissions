class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "[":"]", "{":"}"}
        for l in s:
            if l in pairs:
                stack.append(pairs[l])
            if l in ")]}":
                if not stack or stack.pop() != l:
                    return False
        return not stack