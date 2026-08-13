class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""

        for char1,char2 in zip(strs[0],strs[-1]):
            if char1 == char2:
                prefix += char1
                continue
            else:
                break
        return prefix
