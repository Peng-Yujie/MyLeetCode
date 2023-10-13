class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        int persize = words[0].length();
        int totalsize = persize * words.size();
        int checklen = s.length() - totalsize;
        vector<int> ans;
        if (checklen < 0){
            return ans;
        }

        unordered_map<string, int> wordsmap;
        for(string w : words){
            wordsmap[w]++;
        }

        for(int i = 0; i <= checklen; i++){
            unordered_map<string, int> wordscopy = wordsmap;
            int count = 0;
            for(int j = i; j < s.length(); j += persize){
                string w = s.substr(j,persize);
                if(wordscopy[w] > 0){
                    count++;
                    wordscopy[w]--;
                } else {
                    break;
                }
            }
            if(count == words.size()){
                ans.push_back(i);
            }
        }
        
        return ans;
    }
};