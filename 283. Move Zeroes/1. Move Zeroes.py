class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        
        for i in range(len(nums)) : 
            if nums[i] == 0 : 
                count += 1
        
        locate = 0
        
        for i in range(len(nums)) : 
            if nums[i] != 0 : 
                nums[locate] = nums[i]
                locate += 1
        
        for i in range(count) : 
            nums[len(nums)-i-1] = 0
        
        return nums