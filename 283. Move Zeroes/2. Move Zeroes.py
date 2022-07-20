class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        for i, n in enumerate(nums):
            nums[i] = 0
            if n != 0:
                nums[count] = n
                count += 1
        
        return nums