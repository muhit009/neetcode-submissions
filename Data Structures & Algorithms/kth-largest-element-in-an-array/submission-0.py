class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we will look for the idx at len(nums)-k 
        k = len(nums) - k
        def quickSelect(left,right):
            # first swap the values according to the pivot
            #if less than pivot on the left
            # greater than pivot on the right
            pivot, p= nums[right], left
            for i in range(left,right):
                if nums[i] <= pivot:
                    nums[i],nums[p] = nums[p], nums[i]
                    p = p+1
            #then change the pivot index after everything, so that  we can say on the 
            #left of the pivot everything is less and on the right everything is greater
            nums[p],nums[right] = nums[right], nums[p]

            #now check if p>k or p<k which proves k is greater or less than the k
            #then recursively use the function again
            if p<k: return quickSelect(p+1, right)
            elif p>k: return quickSelect(left, p-1)
            else: return nums[p]
        return quickSelect(0, len(nums)-1)
                
                
             
