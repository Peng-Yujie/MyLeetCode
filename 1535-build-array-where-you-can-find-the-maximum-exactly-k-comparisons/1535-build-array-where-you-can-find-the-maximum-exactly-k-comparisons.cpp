class Solution {
public:
    int numOfArrays(int n, int m, int k) {
        int N = n, M = m, K = k;
        long long dp[n][m+1][k+1];
        long long mod = 1e9 + 7;

        for (int i = 0; i < N; i++)
            for (int j = 1; j <= M; j++)
                for (int k = 0; k <= K; k++)
                    dp[i][j][k] = 0;

        for (int j = 1; j <= M; j++)
            dp[0][j][1] = 1;
        
        for (int i = 1; i < N; i++)
            for (int j = 1; j <= M; j++)
                for (int k = 1; k <= K; k++){
                    // if the last one is the biggest one
                    for (int l = 1; l < j; l++){
                        dp[i][j][k] = (dp[i][j][k] + dp[i-1][l][k-1]) % mod;
                    }
                    // if the last one is not the biggest one, then the value can be 1 to j
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j][k] * j) % mod;
                }

        long long res = 0;
        for (int j = 1; j <= M; j++)
            res = (res + dp[N-1][j][K]) % mod;
        
        return res;
    }
};