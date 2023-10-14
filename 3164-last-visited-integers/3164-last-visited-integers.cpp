class Solution {
public:
    vector<int> lastVisitedIntegers(vector<string>& words) {
        vector<int> ans;
        vector<int> nums;
        int nc = 0, k = 0;
        for(string s : words){
            if(s != "prev"){
                k = 0;
                nc++;
                int n = stoi(s);
                nums.push_back(n);
            } else {
                k++;
                if(k>nc){
                    ans.push_back(-1);
                } else {
                    ans.push_back(nums[nc-k]);
                }
            }
        }
        return ans;
    }
};