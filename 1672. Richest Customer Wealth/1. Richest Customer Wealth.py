class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        large = 0
        for i in range(len(accounts)) : 
            if sum(accounts[i]) > large : 
                large = sum(accounts[i])
        
        return large