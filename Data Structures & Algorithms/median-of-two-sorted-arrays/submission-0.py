class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b =nums1, nums2
        total = len(a)+len(b)
        half = total // 2
        if len(b)<len(a):
            a,b= b,a
        left, right =0, len(a)-1
        while True:
            mid1 = (left+right)//2
            mid2 = half - mid1 -2
            aleft = a[mid1] if mid1>=0 else float("-inf")
            aright = a[mid1+1] if mid1+1< len(a) else float("inf")
            bleft =b[mid2] if mid2>= 0 else float("-inf")
            bright = b[mid2+1] if mid2+1 < len(b) else float("inf")

            if aleft<=bright and bleft<=aright:
                if total %2:
                    return min(aright,bright)
                return (min(aright,bright) + max(aleft,bleft))/2
            elif aleft>=bright:
                right = mid1-1
                
            else:
                left = mid1 +1
