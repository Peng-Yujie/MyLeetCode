class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            // remove duplicate elements
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int diff = 0 - nums[i];
            int j = i + 1, k = nums.length - 1;
            while(j<k){
                if (nums[j] + nums[k] == diff) {
                    res.add(Arrays.asList(nums[i],nums[j],nums[k]));
                    // remove duplicate elements
                    while(j < k && nums[j] == nums[j+1]){
                        j++;
                    }
                    while(j < k && nums[k] == nums[k-1]){
                        k--;
                    }
                    j++;
                    k--;
                } else if (nums[j] + nums[k] > diff) {
                    k--;
                } else {
                    j++;
                }
            }
        }
        return res;
    }
}
