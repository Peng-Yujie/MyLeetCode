class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.length() == 0){
            return 0;
        }
        set<char> subs;
        int left = 0, right = 0;
        int maxlength = 0;
        while(right < s.length()){
            if (subs.count(s[right]) == 0){
                subs.insert(s[right]);
                maxlength = max(maxlength, (int)subs.size());
                right++;
            } else {
                subs.erase(s[left]);
                left++;
            }
        }
        return maxlength;
    }
};