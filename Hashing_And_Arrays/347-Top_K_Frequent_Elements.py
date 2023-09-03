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
        for i in range(k):
            rlist.add(nums.pop()[0])
        
        return(rlist)
        #
    
        # NC NOTES
        #  Above solution is done in n*log(n) time  , Can be done in O(n)
        #  Using modified bucket Sort 
        # ARRAY using COUNT as INDEX and the number as THE VALUE'
        # This solution uses more memory --> but lower time complexity (trade off)
        
    def NCtopKFrequent(self,nums,k):
        count={}
        freq=[[] for i in range(len(nums)+1)]
        
        for num in nums:
            count[num]=1+count.get(num,0)
        for n,c in count.items():
            freq[c].append(n)
            
        result=[]
        # Loop from the end of the frequency list
        #  range(stat,stop,step)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                result.append(n)
                if len(result)==k:
                    return result
                
        



if __name__=="__main__":
    test=Solution()
    print(test.NCtopKFrequent([4,1,-1,2,-1,2,3],2))