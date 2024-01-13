class Solution {
public:
    int minSteps(string s, string t) {
        // count each char in s
        // e.g. a: 1, b:10, c:3;
        // count each char in t
        // a:1, b: 8, c: 5;
        // count the minimum number
        // if s[a] > t[a]

        unordered_map<char, int> maps;
        unordered_map<char, int> mapt;
        int count = 0;
        for(char ch : s){
            maps[ch]++;
        }
        for(char ch : t){
            mapt[ch]++;
        }
        for(auto pair : maps){
            if(mapt.find(pair.first) != mapt.end()){
                if(maps[pair.first] == mapt[pair.first]){
                    count += maps[pair.first];
                } else {
                    count += min(maps[pair.first], mapt[pair.first]);
                }
            }
        }
        return s.size() - count;
    }
};