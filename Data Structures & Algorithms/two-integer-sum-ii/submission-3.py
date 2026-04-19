class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        j =  length-1
        i = 0
        while(i!=j): 
            twoSum = numbers[i]+numbers[j]
            if(twoSum == target): 
                return [i+1, j+1]
            if(twoSum<target):
                i+=1
            elif(twoSum>target): 
                j-=1
        return []