class Solution:
    def maskPII(self, s: str) -> str:
        idx = s.find("@")
        if idx >= 0:
            return f"{s[0].lower()}*****{s[idx-1:].lower()}"
        else:
            s = s.translate(str.maketrans('','',"+- ()"))
            return f"{['', '+*-', '+**-', '+***-'][len(s) -10]}***-***-{s[-4:]}"

