class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}
        res = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
            
        for element in stack:
            mapping[element] = -1
            
        for i in range(len(nums1)):
            res.append(mapping[nums1[i]])
        
        return res