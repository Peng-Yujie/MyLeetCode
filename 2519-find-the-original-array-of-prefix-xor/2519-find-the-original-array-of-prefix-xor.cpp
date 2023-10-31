class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int n = pref.size();
        vector<int> ans(n);
        ans[0] = pref[0];

        for(int i = 1; i < n; i++){
            ans[i] = pref[i] ^ pref[i-1];
        }
        return ans;
    }
};

/**
* if x^y = z
* 1: (x^y)^y = z^y
* 2: (x^y)^y = x^(y^y) = x
* now we have: x = z^y

*/