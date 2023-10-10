class Solution {
public:
    int minOperations(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int diff = nums.size() - 1;

        vector<int> uniq;
        uniq.push_back(nums[0]);
        for(int i = 1; i < nums.size(); i++)
            if(nums[i] != nums[i-1])
                uniq.push_back(nums[i]);

        int ans = INT_MAX;
        for(int i = 0; i < uniq.size(); i++){
            int low = i, high = uniq.size() - 1;
            while(low + 1 < high){
                int mid = low + (high - low)/2;
                if(uniq[mid] <= uniq[i] + diff){
                    low = mid;
                } else {
                    high = mid - 1;
                }
            }

            if(uniq[high] <= uniq[i] + diff){
                ans = min(ans, diff - (high - i));
            } else {
                ans = min(ans, diff - (low - i));
            }
        }

        return ans;
    }
};