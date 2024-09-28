class Solution {
    public int jump(int[] nums) {
        int curEnd = 0, curLongest = 0, count = 0;
        for (int i = 0; i< nums.length-1; i++){
            //find how far the current index can reach
            curLongest = Math.max(curLongest, nums[i]+i);
            //when the index meets the current end, we check the length so far
            if (i == curEnd){
                curEnd = curLongest;
                count++;
            }
        }
        return count;
    }
}