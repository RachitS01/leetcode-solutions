
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeats = -(-len(b)//len(a))

        repeated_a = a*repeats

        if b in repeated_a:
            return repeats
        if b in (repeated_a + a):
            return repeats + 1

        return -1
