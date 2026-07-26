class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        diff = inf 
        cur_sum = None
        for i in range(n-2):
            x = nums[i]
            if x+nums[i+1]+nums[i+2]>target:
                if (x+nums[i+1]+nums[i+2])-target<diff:
                    diff = (x+nums[i+1]+nums[i+2])-target
                    cur_sum = (x+nums[i+1]+nums[i+2])
                break
            if x+nums[-1]+nums[-2]<target:
                if target-(x+nums[-1]+nums[-2])<diff:
                    diff = target-(x+nums[-1]+nums[-2])
                    cur_sum = x+nums[-1]+nums[-2]
                continue
            left,right = i+1,n-1
            while left<right:
                if nums[left]+nums[right]+x==target:
                    return target
                elif nums[left]+nums[right]+x>target:
                    if nums[left]+nums[right]+x-target<diff:
                        diff = nums[left]+nums[right]+x-target
                        cur_sum = nums[left]+nums[right]+x
                    right -= 1
                else:
                    if target-(nums[left]+nums[right]+x)<diff:
                        diff = target-(nums[left]+nums[right]+x)
                        cur_sum = nums[left]+nums[right]+x
                    left += 1
        return cur_sum
