class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        check = nums
        if check == sorted(nums) or check == sorted(nums, reverse = True) : 
            return True
        else : 
            return False