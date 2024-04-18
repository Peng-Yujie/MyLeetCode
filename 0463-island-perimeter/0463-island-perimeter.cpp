class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int res = 0;
        for (int row = 0; row < grid.size(); row++ ) {
            for (int col = 0; col < grid[row].size(); col++) {
                if (grid[row][col] == 1) {
                    res += 4;
                    if (row > 0 && grid[row-1][col] == 1) res -= 2;
                    if (col > 0 && grid[row][col-1] == 1) res -= 2;
                }
            }
        }
        return res;
    }
};