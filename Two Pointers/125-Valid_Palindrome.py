class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s=''.join([c for c in s if c.isalnum()]).lower()
      
        if s==s[::-1]:
            return True
        return False
        # Uses Built In Function
        # Uses Extra Memory

    def NCisPalindrome(self, s):
        # Memory of O(1) and Time : O(n)
        # Two pointer Solution
        # L and R Pointer (Increment Left pointer , decrement Right Pointer)
        # Check for equality via ASCII values , skip non alphanum chars
        #  0-9 : 48-57
        left,right=0 , len(s)-1
        
        while left<right:
            
            while left<right and not self.isAlphaNum(s[left]):
                left+=1
            while right>left and not self.isAlphaNum(s[right]):
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left,right=left+1,right-1
        return True
        
    def isAlphaNum(self,c):
       return( ord('A') <= ord(c) <= ord('Z') or \
               ord('a') <= ord(c) <= ord('z') or \
               ord('0') <= ord(c) <= ord('9'))
        
        
        
        
          
    

if __name__ == "__main__":
    test=Solution()
    print(test.NCisPalindrome("0P"))
        