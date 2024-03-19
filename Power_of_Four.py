class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n<0:
        #     return False
        # if bin(n).count('1')!=1:
        #     return False
        # if len(bin(n))%2==0:
        #     return False
        # return True
        
        return bin(n).count('1')==1 and (n-1)%3 == 0