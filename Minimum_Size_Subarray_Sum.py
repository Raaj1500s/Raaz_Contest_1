class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        start = 0
        ans = float('inf')
        end = 0
        while end < len(nums):
            total += nums[end]
            while total >= target:
                ans = min(ans,end-start+1)
                total -= nums[start]
                start += 1
            end += 1
        return ans if ans != float('inf') else 0