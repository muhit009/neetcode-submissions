class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:]) # perms = [[2,3], [3,2]] etc.
        res = []
        for p in perms: # we will get something like [3,2]
            for i in range(len(p) + 1): # +1 because we can add an element at the last of the element
                p_copy = p.copy()
                # now will add the first element new in every index
                p_copy.insert(i, nums[0])
                res.append(p_copy)


        return res