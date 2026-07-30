class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_multiplier = 0

        for i in range(len(s)):
            if s[i].isdigit():
                current_multiplier = current_multiplier*10 + int(s[i])
            elif s[i].isalpha():
                current_string += s[i]

            elif s[i] == "[":
                stack.append((current_string,current_multiplier))
                current_string = ""
                current_multiplier = 0
            elif s[i] == "]":
                prev_string,prev_multiplier = stack.pop()
                current_string *= prev_multiplier

                current_string = prev_string + current_string

        return current_string
