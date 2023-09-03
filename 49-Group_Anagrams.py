class Solution(object):
    def groupAnagrams(self, strs:list):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # Sorting -->  m * n log n  (m=number of strings , n=length of each string)
        # Hashmap Method --> m*n*26 --> m*n --> m=number of strings , n=length of string
        result=dict()
        #  Map charCount to list of Anagrams
        
        for s in strs:
            count=list([0]*26)
          
      
            for char in s:
                count[ord(char) - ord("a")]+=1 # getting correct index via ascii values
            count=tuple(count)
            if result.setdefault(count)!=None:
                 result.get(count).append(s)
            else:
                result.update({count:[s]})
        return list(result.values())
        
        
        
    
test=Solution()
test.groupAnagrams(["eat","tea","tan","ate","nat","bat"])