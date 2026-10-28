class Solution:
    from collections import defaultdict

    
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = defaultdict(int)

        for v in nums:
            if v in myDict:
                return True
            myDict[v]
        return False

       
            
            


        