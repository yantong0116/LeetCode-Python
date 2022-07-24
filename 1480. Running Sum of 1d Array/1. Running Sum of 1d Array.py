class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        
        for i in range(len(nums)) : 
            count = 0
            for j in range(i+1) : 
                count += nums[j]
            res.append(count)
        
        return res