class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        int start = -1, end = -1;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] == target){
                start = mid;
                right = mid - 1;
            } else if (nums[mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        left = 0;
        right = nums.size()-1;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(nums[mid] == target){
                end = mid;
                left = mid + 1;
            } else if (nums[mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        vector<int> res;
        res.push_back(start);
        res.push_back(end);
        return res;
    }
};