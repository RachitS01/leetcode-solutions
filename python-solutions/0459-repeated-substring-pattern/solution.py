class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
            doubled = s+s
            doubled = doubled[1:-1]

            if  doubled.find(s) !=-1:
                return True
            
            return False

