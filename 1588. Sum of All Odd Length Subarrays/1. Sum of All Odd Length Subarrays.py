class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)

        for i in range(3, len(arr) + 1, 2) :             
            for j in range(0, len(arr) - i + 1) :
                for k in range(i) : 
                    res += arr[j + k]
        return res