class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int count = 0;
        unordered_map<int, int> m;
        for (int i = 0; i < nums.size(); i++){
            if (m.find(nums[i]) == m.end()){
                m.insert({nums[i], 1});
            } else {
                count += m.at(nums[i]);
                m.at(nums[i])++;
            }
        }
        return count;
    }
};