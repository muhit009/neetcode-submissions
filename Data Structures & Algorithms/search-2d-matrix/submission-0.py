class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            print('mid', mid)
            row = mid // n
            print('row and n',row,n)
            col = mid % n
            print('column and n',col, n)
            mid_value = matrix[row][col]
            print('mid value',row, col, mid_value)

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
