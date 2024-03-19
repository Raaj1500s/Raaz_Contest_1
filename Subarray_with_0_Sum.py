class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        dic = {0:-1}
        su = 0
        for ind,i in enumerate(arr):
            su += i
            if su in dic:
                return True
            dic[su] = ind
        return False