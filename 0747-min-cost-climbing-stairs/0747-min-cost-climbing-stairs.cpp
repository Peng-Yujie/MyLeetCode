class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int dp[cost.size()+1];
        memset(dp,0,sizeof dp);
        for(int i = 2; i < cost.size()+1; i++){
            dp[i] = min(dp[i-1] + cost[i-1],dp[i-2] + cost[i-2]); 
        }
        return dp[cost.size()];
    }
};