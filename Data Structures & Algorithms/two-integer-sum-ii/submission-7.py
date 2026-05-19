class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = len(numbers) - 1
        num_sum = numbers[index1] + numbers[index2]

        while (target != num_sum and 
            index1 < index2):

            if num_sum < target:
                index1 += 1
            else:
                index2 -= 1
            num_sum = numbers[index1] + numbers[index2]

        if num_sum == target:
            return [index1+1, index2+1]
        return []