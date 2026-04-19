class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countLookUp = {}
        frequencyList = [[] for _ in range(len(nums) + 1)]
        for i in nums:
            if(countLookUp.get(i)==None):
                countLookUp[i] = 1
                frequencyList[1].append(i)
            else:
                prevCount = countLookUp[i]
                print(prevCount)
                frequencyList[prevCount].remove(i)
                frequencyList[prevCount+1].append(i)
                countLookUp[i] += 1
                
        returnList = []
        for i in range(len(nums)):
            if(frequencyList[len(nums)-i]!=[]):
                for x in frequencyList[len(nums)-i]:
                    if(k>0):
                        returnList.append(x)
                        k-=1
                    else:
                        return returnList

        return returnList