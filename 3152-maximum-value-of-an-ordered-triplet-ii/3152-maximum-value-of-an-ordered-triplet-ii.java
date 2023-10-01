class Solution {
    public long maximumTripletValue(int[] nums) {   
        long res = 0, maxleft = 0, maxright = 0;
        for (int num : nums){
            res = Math.max(res, 1L * maxleft * num);
            maxleft = Math.max(maxleft, maxright - num);
            maxright = Math.max(maxright, num);
        }
        return res;
    }
}
