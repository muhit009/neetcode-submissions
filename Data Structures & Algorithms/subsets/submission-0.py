class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(idx):
            if idx>=len(nums):
                # print('subset',subset)
                # print('copy', subset)
                res.append(subset.copy())
                return
            #include the decision    
            subset.append(nums[idx])
            # print('append', subset)
            dfs(idx+1)
            #exclude the decision
            subset.pop()
            # print('pop', subset)
            dfs(idx+1)
        dfs(0)
        return res
        