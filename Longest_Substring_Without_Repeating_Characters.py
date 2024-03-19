class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = 0
        length = 0
        maxii = 0
        for i in range(len(s)):
            if s[i] not in s[ind:i]:
                maxii = max(maxii,i-ind+1)
            else:
                while s[ind]!=s[i]:
                    ind+=1
                ind+=1
        maxii = max(length,maxii)
        return maxii