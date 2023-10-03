class Solution {
public:
    string reverseWords(string s) {
        stack<char> chs;
        string res;
        for (char c : s){
            if (c != ' '){
                chs.push(c);
            } else {
                while(!chs.empty()){
                    res.push_back(chs.top());
                    chs.pop();
                }
                res.push_back(' ');
            }
        }
        while(chs.size()>0){
            res.push_back(chs.top());
            chs.pop();
        }
        return res;
    }
};