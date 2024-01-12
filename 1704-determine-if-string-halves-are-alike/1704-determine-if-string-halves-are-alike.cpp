class Solution {
public:
    bool halvesAreAlike(string s) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int l = 0, r = 0;
        int mid = s.length()/2;
        for(int i = 0; i < mid; i++){
            if (vowels.count(s[i])) l++;
            if (vowels.count(s[i+mid])) r++;
        }
        return l == r;
    }
};