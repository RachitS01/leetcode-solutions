class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0]*101
        for num in nums:
            freq[num] += 1

        for i in range(1,101):
            freq[i] = freq[i-1]+freq[i]

        output = []
        for j in nums:
            if j == 0:
                output.append(0)
            else:    
                output.append(freq[j-1])
        
        return output
            
