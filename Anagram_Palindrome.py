from collections import Counter 
class Solution:

    def isPossible(self, S):
        a=Counter(S)
        a=dict(a)
        c=0
        for v in a.values():
            if v%2==1:
                c+=1
        if c>1:
            return False
        return True