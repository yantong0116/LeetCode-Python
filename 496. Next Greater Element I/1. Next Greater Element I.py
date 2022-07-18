class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums1)) : 
            k = nums2.index(nums1[i])
            check = 0
            
            for j in range(k + 1, len(nums2)) : 
                if nums2[j] > nums1[i] and check == 0: 
                    check = 1
                    res.append(nums2[j])
                    
            if check == 0 : 
                res.append(-1)
                
        return res