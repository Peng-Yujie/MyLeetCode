class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()){
            return "";
        }
        unordered_map<char, int> map;
        for(int i=0; i<t.length(); i++){
            map[t[i]]++;
        }
        int count=0, start=0, left=0, right=0, min_length = INT_MAX;
        while ( right < s.length() ) {
            if (map[s[right]] > 0) {
                count++;
            }
            map[s[right]]--;
            if (count == t.length()) {
                while (left < right && map[s[left]]<0) {
                    map[s[left]]++;
                    left++;
                }
                if (min_length > (right - left)){
                    min_length = right - left + 1;
                    start = left;
                }
                map[s[left]]++;
                left++;
                count--;
            }
            right++;
        }
        if (min_length > s.length()){
            return "";
        } else {
            return s.substr(start, min_length);
        }

    }
};