class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int M = nums1.size();
        int N = nums2.size();
        int dp[M+1][N+1];
        memset(dp, 0, sizeof dp);

        int min1 = INT_MAX;
        int max1 = INT_MIN;
        int min2 = INT_MAX;
        int max2 = INT_MIN;
        for (int n : nums1){
            max1 = max(max1,n);
            min1 = min(min1,n);
        }
        for (int n : nums2){
            max2 = max(max2,n);
            min2 = min(min2,n);
        }
        if ((max1 < 0 && min2 > 0) || (min1 >0 && max2 < 0)){
            return max(max1 * min2, max2 * min1);
        }

        for(int i = M - 1; i >= 0; i--){
            for(int j = N - 1; j >= 0; j--){
                int dotProduct = nums1[i] * nums2[j] + dp[i+1][j+1];
                dp[i][j] = max({dotProduct, dp[i+1][j], dp[i][j+1]});
            }
        }
        
        int res = dp[0][0];
        return res;

    }
};