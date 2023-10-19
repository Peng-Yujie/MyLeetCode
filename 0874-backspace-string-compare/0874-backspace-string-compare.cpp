class Solution {
public:
    bool backspaceCompare(string s, string t) {
        vector<char> vs;
        vector<char> vt;
    
        for(char c : s){
            if(c != '#'){
                vs.push_back(c);
            } else if(vs.size()>0) {
                vs.pop_back();
            }
        }

        for(char c : t){
            if(c != '#'){
                vt.push_back(c);
            } else if(vt.size()>0) {
                vt.pop_back();
            }
        }

        if(vs.size()!=vt.size()){
            return false;
        }
        for(int i=0;i<vs.size();i++){
            if(vs[i]!=vt[i]){
                return false;
            }
        }
        return true;
    }
};