class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l,r = 0,0

        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            #left value is out of bounds? (left value form the window)
            if l>q[0]:
                q.popleft()
            if (r+1) >= k:
                output.append(nums[q[0]])
                l = l+1
            r = r+1
        return output
            
