class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()[::-1]

        answer = [s[i:i+k] for i in range(0,len(s),k) ]
        
        return "-".join(answer)[::-1]






        
