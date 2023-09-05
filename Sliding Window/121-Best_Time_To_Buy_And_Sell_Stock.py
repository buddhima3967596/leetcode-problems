class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Too Inefficient
        # You're checking every N against every other n
        
        diff=0
        
        
        for dayCompare in range(0,len(prices)-1):
                print(prices[dayCompare],prices[dayCompare+1])
                if prices[dayCompare+1]-prices[dayCompare]>diff:
                    diff=prices[dayCompare+1] - prices[dayCompare]
        return diff
    
    def NCmaxProfit(self,prices):
        # Two Pointer Problem
        # Left Point on Day 1 , Right Pointer on Day 2
        # Left=Buy
        # Right=Sell
        #  if Buy < Sell --> Let Buy=Sell , and Sell=Day+1
        # MaxProfit 
        # Mem: O(1)
        # Time : O(n)
        
        leftBuy,rightSell=0,1
        maxProfit=0
        
        while rightSell<len(prices):
            if prices[leftBuy]<prices[rightSell]:
                profit=prices[rightSell]-prices[leftBuy]
                maxProfit=max(maxProfit,profit)
            else:
                leftBuy=rightSell
                # Go to lowest price known (to maximize profit)
            rightSell+=1
        return maxProfit
        
        
        pass
if __name__=="__main__":
    test=Solution()
    print(test.maxProfit([7,1,5,3,6,4]))