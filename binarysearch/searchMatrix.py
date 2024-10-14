class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot = len(matrix)-1
        right = len(matrix[0])-1
        left = 0
        top = 0

        while top <= bot:
            mid = (top+bot)//2

            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break
            elif matrix[mid][-1] < target:
                top = mid+1
            elif matrix[mid][0] > target:
                bot = mid-1
            else:
                break

        row = (top+bot)//2

        while left <= right:        
            mid = (left+right)//2
            if matrix[row][mid] > target:
                right = mid-1
            elif matrix[row][mid] < target:
                left = mid+1
            else:
                return True
        
        return False