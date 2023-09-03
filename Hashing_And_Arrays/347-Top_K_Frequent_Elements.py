class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rlist=set()
        fdict=dict()
    
        # no need to sort before hand
        for item in nums:
            if item not in fdict:
                fdict[item]=0
            fdict[item]+=1
       
        nums=fdict.items()
        nums=sorted(nums,key=lambda item: item[1])
        #  You don't need to sort the entire list/dict how would you implement it?
        #  
        for i in range(k):
            rlist.add(nums.pop()[0])
        
        return(rlist)
    
        # NC NOTES
        # 




if __name__=="__main__":
    test=Solution()
    print(test.topKFrequent([4,1,-1,2,-1,2,3],2))