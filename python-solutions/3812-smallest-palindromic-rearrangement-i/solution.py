class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        char_counts = [0]*26
        for i in range(len(s)):
            char_counts[ord(s[i])-ord('a')] += 1

        left_half = []
        middle_char = ''
        for i in range(26):
            char = chr(ord('a')+i)
            count  = char_counts[i]

            if count %2 != 0:
                middle_char = char

            left_half.append(char*(count//2))

        left = ''.join(left_half)

        return left + middle_char + left[::-1]
