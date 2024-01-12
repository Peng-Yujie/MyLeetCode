class Solution {
public:
    bool halvesAreAlike(string s) {
        string vowels = "aeiouAEIOU";
        int l = 0, r = 0;
        for(int i = 0; i < s.length()/2; i++){
            if (vowels.find(s[i])!= string::npos) l++;
            if (vowels.find(s[s.length()/2+i])!= string::npos) r++;
        }
        return l == r;
    }
};