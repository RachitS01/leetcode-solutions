import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        min_heap = [(nums1[0]+nums2[0],0,0)]
        n1,n2 = len(nums1),len(nums2)

        while len(res) < k  and min_heap:
            current_sum, i, j = heapq.heappop(min_heap)
            res.append([nums1[i],nums2[j]])
            
            if j == 0 and i+1 < n1:
                heapq.heappush(min_heap,(nums1[i+1] + nums2[j], i+1 , j ))
            if j+1 < n2:
                heapq.heappush(min_heap,(nums1[i] + nums2[j+1], i , j+1 ))

        return res
