class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        vector<string> line;
        int lineWidth = 0;
        int i = 0;
        while(i < words.size()){
            if(lineWidth == 0){
                line.push_back(words[i]);
                lineWidth = words[i].length();
            }
            if(i == (words.size() - 1)){
                string s = "";
                for(int m = 0; m < line.size(); m++)
                        s += line[m];
                for(int n = 0; n < (maxWidth - lineWidth); n++)
                        s += " ";
                ans.push_back(s);
                i++;
            } else if (words[i+1].length() + 1 + lineWidth > maxWidth){
                //Add line to ans
                if(line.size() == 1){
                    string s = line[0];
                    for(int n = 0; n < (maxWidth - lineWidth); n++)
                        s += " ";
                    ans.push_back(s);
                } else {
                int spaceBetween = (maxWidth - lineWidth) / (line.size() - 1);
                int spaceExtra = (maxWidth - lineWidth) % (line.size() - 1);
                for(int m = 0; m < line.size() - 1; m++)
                    for(int n = 0; n < spaceBetween; n++)
                        line[m] += " ";
                for(int m = 0; m < spaceExtra; m++)
                    line[m] += " ";
                string s = "";
                for(int m = 0; m < line.size(); m++)
                    s += line[m];
                ans.push_back(s);
                }
                line.clear();
                lineWidth = 0;
                i++;
            } else {
                i++;
                line.push_back(" " + words[i]);
                lineWidth += (words[i].length() + 1);
            }
        }
        return ans;
    }
};