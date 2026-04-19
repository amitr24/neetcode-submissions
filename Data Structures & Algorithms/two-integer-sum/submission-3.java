class Solution {
    public int[] twoSum(int[] nums, int target) {
        int minValueNeeded = target;
        int[] achieveTarget = new int [nums.length];
        for(int i = 0; i < nums.length; i++)
            achieveTarget[i] = target;
        
        for(int i = 0; i < nums.length; i++){
            achieveTarget[i] -= nums[i];
            if(minValueNeeded>achieveTarget[i]){
                minValueNeeded = achieveTarget[i];
            }
            if(minValueNeeded<=nums[i]){
                for(int j = 0; j < i; j++){
                    if(achieveTarget[j]==nums[i])
                        return new int[]{j, i};
                }   
            }
        }
        return new int[]{};
    }
}
