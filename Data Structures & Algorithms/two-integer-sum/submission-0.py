class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydict = {}
        for i,v in enumerate(nums):
            possibleAnswer = target - v
            if possibleAnswer in mydict:
                return [mydict[possibleAnswer],i]
                
            mydict[v] = i
        


        