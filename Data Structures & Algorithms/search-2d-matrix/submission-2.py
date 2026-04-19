import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                val = nums[mid] - target
                if val > 0:
                    high = mid - 1
                elif val == 0:
                    return mid
                else:
                    low = mid + 1
            return -1

        def range_search(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                val = nums[mid] - target
                if val > 0:
                    high = mid - 1
                elif val == 0:
                    return mid
                else:
                    low = mid + 1
            return low

        matrix = np.array(matrix)
        last_column = matrix[:, -1]

        row = range_search(last_column, target)
        if row < 0 or row >= len(matrix):
            return False  # target smaller than first row
        row_values = matrix[row, :]
        return search(row_values, target) != -1
