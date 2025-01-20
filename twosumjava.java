class Solution {
    public int[] twoSum(int[] nums, int target) {

        // Create hashmap
        Map<Integer, Integer> map = new HashMap<>();

    /*
    Directions: 

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

     */
        // Iterate through the nums list.
        for(int i =0;i<nums.length;i++){
            // get current value 
            int curr = nums[i];
            // Minus target by current to get a compatible value.
            int x = target - curr;
            // Find that compatible value v such that curr + v = target
            if(map.containsKey(x)){ // Using hashmap allows easy searching.
                // if found return the twosum.
                // return in array format.
                return new int[] {map.get(x), i};
            }
            // else put i in curr in map.
            map.put(curr, i);
        }
        return null;