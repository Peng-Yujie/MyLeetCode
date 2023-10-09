class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = -1, end = -1;
        bool isFound = false;
        for (int i = 0; i< nums.size(); i++){
            if(!isFound && nums[i] == target){
                start = end = i;
                isFound = true;
            } else if (nums[i] == target) {
                end = i;
            }
        }
        vector<int> res;
        res.push_back(start);
        res.push_back(end);
        return res;
    }
};