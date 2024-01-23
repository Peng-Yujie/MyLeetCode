class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<int> chs(26,0);
        return helper(0, arr, chs);
    }

    int helper(int i, vector<string>& arr, vector<int> chs) {
        if (i == arr.size()) return 0;
        int skip = helper(i+1, arr, chs);
        for (char ch : arr[i]) {
            if (chs[ch - 'a']) return skip;
            chs[ch - 'a'] = 1;
        }
        int keep = helper(i+1, arr, chs) + arr[i].length();
        return max(skip, keep);
    }
};