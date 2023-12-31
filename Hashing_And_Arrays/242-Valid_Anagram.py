class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
       
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
    
        # Other option is sort each string and compare it

    
test=Solution()

test.isAnagram("aacc","ccac")