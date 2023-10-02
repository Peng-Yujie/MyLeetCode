class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> ans;
        int left = 0, right = n-1, top = 0, bottom = m-1;
        while(left <= right && top <= bottom){
            // move to right
            for(int i = left; i <= right; i++){
                ans.push_back(matrix[top][i]);
            }
            top++;

            // move to bottom
            for(int i = top; i <= bottom; i++){
                ans.push_back(matrix[i][right]);
            }
            right--;

            // move to left
            if (top<=bottom){
                for(int i = right; i >= left; i--){
                    ans.push_back(matrix[bottom][i]);
                }
                bottom--;
            }

            // move to top
            if (left <= right){
                for(int i = bottom; i >= top; i--){
                    ans.push_back(matrix[i][left]);
                }
                left++;
            }
        }
        return ans;
    }
    
};