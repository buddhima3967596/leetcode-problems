class Solution(object):
    def containsDuplicate(self,nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Trade off between space complexity and time complexity 
        # N
        contains=set()
        for item in nums:
            if item in contains:
                return True
            contains.add(item) 
        return False
        
        
        
test=Solution()   

if (test.containsDuplicate([1,2,3,1])):
        print("Bruh")