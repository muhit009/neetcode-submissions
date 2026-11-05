class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftmax = rightmax= height[i]

            for j  in range(i):
                leftmax = max(leftmax,height[j])
            for j in range(i+1, n):
                rightmax = max(rightmax,height[j])
            
            res += min(leftmax,rightmax) - height[i]
        return res