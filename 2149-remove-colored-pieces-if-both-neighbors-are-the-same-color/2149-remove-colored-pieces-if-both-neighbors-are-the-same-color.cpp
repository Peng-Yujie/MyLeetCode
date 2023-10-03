class Solution {
public:
    bool winnerOfGame(string colors) {
        // remove a A if there is AAA
        // if As are seperated by Bs, since Bs cannot be all removed, it is no need to consider this situation
        // So that, every time search if there is AAA or BBB
        // Solution 1: search a color, remove it and rebuilt colors -> complex
        // Solution 2: calculate the possible times of A and B, return true if A > B
        int acount = 0, bcount = 0;
        int aturn = 0, bturn = 0;
        for(char c : colors){
            if (c=='A'){
                bcount = 0;
                acount++;
                if (acount>=3){
                    aturn++;
                }
            } else {
                acount = 0;
                bcount++;
                if (bcount>=3){
                    bturn++;
                }
            }
        }
        return aturn > bturn;
    }
};