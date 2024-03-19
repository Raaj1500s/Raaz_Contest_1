class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = [height[0]]
        for i in range(1,len(height)):
            left.append(max(left[-1],height[i]))
        right = [height[-1]]
        for i in range(len(height)-2,-1,-1):
            right.append(max(right[-1],height[i]))
        right = right[::-1]
        print(left,right)
        for i in range(1,len(height)-1):
            l = i-1
            r = i+1
            l_maxi = left[i-1]
            r_maxi = right[i+1]
            
            if l_maxi > height[i] and r_maxi > height[i]:
                print(i)
                print(l_maxi,r_maxi)
                ans += min(l_maxi,r_maxi)-height[i]
        return ans