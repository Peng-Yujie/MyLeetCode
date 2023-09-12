class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> set;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') { // Use single quotes for character '.'
                    if (!set.insert("row" + to_string(i) + board[i][j]).second || !set.insert("col" + to_string(j) + board[i][j]).second || !set.insert("box" + to_string(i/3) + to_string(j/3) + board[i][j]).second) {
                            return false;
                    }
                }
            }
        }
        return true;
    }
};