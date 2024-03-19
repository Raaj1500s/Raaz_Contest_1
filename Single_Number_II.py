class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 2**32-1
        for i in range(32):
            sum = 0
            mask = 1<<i
            for num in nums:
                sum += num&mask
            if sum%3==0:
                res-=mask
        if res >= 2**31:
            res -= 2**32
        return res