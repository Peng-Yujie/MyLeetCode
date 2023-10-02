class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int left = 0, right = n-1, top = 0, bottom = n-1;
        int val = 1;
        vector<vector<int>> ans(n, vector<int>(n));
        while(left <= right && top <= bottom){
            // move to right
            for(int i = left; i <= right; i++){
                ans[top][i] = val++;
            }
            top++;

            // move to bottom
            for(int i = top; i <= bottom; i++){
                ans[i][right] = val++;
            }
            right--;

            // move to left
            if (top<=bottom){
                for(int i = right; i >= left; i--){
                    ans[bottom][i] = val++;
                }
                bottom--;
            }

            // move to top
            if (left <= right){
                for(int i = bottom; i >= top; i--){
                    ans[i][left] = val++;
                }
                left++;
            }
        }
        return ans;
    }
};