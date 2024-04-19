class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        for (int r = 0; r < grid.size(); r++) {
            for (int l = 0; l < grid[r].size(); l++) {
                if (grid[r][l] == '1') {
                    res += 1;
                    if (r > 0 && grid[r-1][l] == '1' || l > 0 && grid[r][l-1] == '1') res -= 1;
                }
            }
        }
        return res;
    }
};