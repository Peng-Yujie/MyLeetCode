class Solution {
    public int rob(int[] nums) {
        int len = nums.length;
        if (len <= 0) {
            return 0;
        } else if (len == 1) {
            return nums[0];
        } else if (len == 2) {
            return Math.max(nums[0],nums[1]);
        } else {
            int[] ans = new int[len];
            ans[0] = nums[0];
            ans[1] = Math.max(nums[0],nums[1]);
            ans[2] = Math.max(nums[0]+nums[2],nums[1]);
            for (int i=3; i<len; i++){
                ans[i] = nums[i] + Math.max(ans[i-2],ans[i-3]);
            }
            return Math.max(ans[len-1], ans[len-2]);
        }
    }
}