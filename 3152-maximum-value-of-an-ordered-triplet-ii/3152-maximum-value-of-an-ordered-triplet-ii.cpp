class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        vector<int> ks(nums.size());
        int maxk = nums[nums.size()-1];
        for (int k = nums.size()-1; k >= 0; k--){
            maxk = max(maxk,nums[k]);
            ks[k] = maxk;
        }
        vector<int> is(nums.size());
        int maxi = nums[0];
        for (int i = 0; i < nums.size(); i++){
            maxi = max(maxi,nums[i]);
            is[i] = maxi;
        }
        long long ans = -1;
        for (int j = 1; j < nums.size() - 1; j++){
            ans = max(ans, static_cast<long long>(is[j-1]-nums[j])*ks[j+1]);
        }
        if (ans >= 0){
            return ans;
        } else {
            return 0;
        }
    }
};