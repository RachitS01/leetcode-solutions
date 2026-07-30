class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(start,path):
            if len(path) == 4 and start == len(s):
                result.append('.'.join(path))

            if len(path) == 4 or start == len(s):
                return

            for length in range(1,4):

                if start + length > len(s):
                    break

                segment = s[start:start+length]

                if int(segment) > 255:
                    continue
                if len(segment) > 1 and segment[0] == "0":
                    continue

                path.append(segment)

                backtrack(start+length,path)

                path.pop()

        backtrack(0,[])

        return result
