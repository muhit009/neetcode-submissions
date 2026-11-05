class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if idx >= len(nums) or total > target:
                return


            curr.append(nums[idx])    
            dfs(idx, curr, total + nums[idx])

            curr.pop()
            dfs(idx+1, curr, total)
        dfs(0, [], 0)
        return res 