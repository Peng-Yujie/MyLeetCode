class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        if (matrix.size() == 1) return matrix[0][0];

        int n=matrix.size();
        vector<vector<int>>dp(matrix);
        for (int i = n - 1; i >= 1; i--) {
            for (int j = 0; j < n; j++) {
                int sum = dp[i][j];
                if (j > 0) {
                    sum = min(sum, dp[i][j - 1]);
                }
                if (j < n - 1) {
                    sum = min(sum, dp[i][j + 1]);
                }
                dp[i - 1][j] += sum;
            }
        }

        int res = dp[0][0];
        for (int n : dp[0]) {
            res = min(res, n);
        }
        return res;
    }
};