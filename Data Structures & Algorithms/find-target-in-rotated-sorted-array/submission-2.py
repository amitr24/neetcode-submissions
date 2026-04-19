class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cut_point = 0
        low = 0 
        high = len(nums) - 1
        arr = nums
        while (low < high):
            mid = (low + high) // 2
            print(f"mid={mid}, arr[mid]={arr[mid]}, low={low}, arr[low]={arr[low]}, high={high}, arr[high]={arr[high]}")
            if arr[mid] < arr[high]:
                high = mid
            elif arr[low] <= arr[mid]: 
                low = mid+1
        
        cut_point = low
        if arr[cut_point] <= target <= arr[-1]:
            low = cut_point
            high = len(nums) - 1
        else:
            low = 0
            high = cut_point - 1
        while (low <= high):
            mid = (low + high) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
            