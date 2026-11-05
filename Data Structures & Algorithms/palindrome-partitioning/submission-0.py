class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = [] #current partition
        
        def dfs(idx):
            if idx>= len(s):
                res.append(part.copy())
                return
            # now for every possible substring
            for j in range(idx,len(s)):
                if self.isPalindrome(s, idx, j):
                    part.append(s[idx:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def isPalindrome(self, s, left,right):
        while left<right:
            if s[left] != s[right]:
                return False
            left,right = left+1, right-1
        return True

