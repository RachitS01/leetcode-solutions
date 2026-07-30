class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []


        total_strings = 3*(2**(n-1))

        if k > total_strings:
            return ""

        choices = ["a","b","c"]

        k-=1
        #step 1: find first letter

        bucket_size = 2**(n-1)
        result.append(choices[k//bucket_size])
        
        k %= bucket_size

        #step2: find remaining n-1 letters
        for i in range(1,n):
            bucket_size = 2**(n-1-i)

            valid_choices = [x for x in choices if x!= result[-1]]
            result.append(valid_choices[k//bucket_size])

            k%=bucket_size

        return "".join(result)
