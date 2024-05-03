class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length-1;
        int maxArea = 0;
        while(left<right){
            int curArea = Math.min(height[left],height[right])*(right-left);
            maxArea = Math.max(curArea, maxArea);
            
            if(height[left]<height[right]){
                left++;
            }else{
                right--;
            }
        }
        return maxArea;
        // return maxArea(height, left, right);
    }
    // public int maxArea(int[] height, int left, int right){
    //     if(right - left == 1){
    //         return Math.min(height[left],height[right]);
    //     } else if(right>left) {
    //         int area = Math.min(height[left],height[right]) * (right-left);
    //         return Math.max(area,Math.max(maxArea(height, left+1, right),maxArea(height, left, right-1)));
    //     } else {
    //         return 0;
    //     }
    // }
}