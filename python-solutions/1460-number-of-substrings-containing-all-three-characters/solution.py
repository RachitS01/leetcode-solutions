class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        tcount = 0
        counts = {'a':0,'b':0,'c':0}
        for right in range(len(s)):
            counts[s[right]] +=1

            while counts['a'] >=1 and counts['b']>=1 and counts['c']>=1:
                tcount += len(s) -right

                counts[s[left]] -= 1
                left += 1
        return tcount
