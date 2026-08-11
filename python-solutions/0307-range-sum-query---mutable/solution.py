class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        
       
        self.tree = [0] * (self.n + 1)
        
       
        self.cache = {} 
        
        for i in range(self.n):
            self.tree[i + 1] = nums[i]
            
        for i in range(1, self.n + 1):
            parent = i + (i & -i)
            if parent <= self.n:
                self.tree[parent] += self.tree[i]

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        
        i = index + 1
        while i <= self.n:
            self.tree[i] += diff
            i += i & -i
            
      
        self.cache.clear() 

    def sumRange(self, left: int, right: int) -> int:
        
        if (left, right) in self.cache:
            return self.cache[(left, right)]
            
      
        def get_prefix_sum(i: int) -> int:
            total = 0
            while i > 0:
                total += self.tree[i]
                i -= i & -i
            return total
            
        res = get_prefix_sum(right + 1) - get_prefix_sum(left)
        
        
        self.cache[(left, right)] = res
        return res
