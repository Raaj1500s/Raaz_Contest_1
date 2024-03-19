class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        mini1 = float('inf')
        mini2 = float('inf')
        for num in nums:
            if num<mini1:
                mini2 = mini1
                mini1 = num
            elif num<mini2:
                mini2 = num
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return max(first*second*third,mini1*mini2*first)