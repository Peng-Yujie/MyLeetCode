class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int count = 0;
        vector<vector<int>> ans;
        int left = cStart, right = cStart, top = rStart, bottom = rStart;
        while (count < rows*cols){
            for(int i = left; i <= right; i++){
                if (i >= 0 && i < cols && top >=0){
                    ans.push_back({top,i});
                    count++;
                }
            }
            right++;
            
            for(int i = top; i<= bottom; i++){
                if (i >= 0 && i < rows && right < cols){
                    ans.push_back({i,right});
                    count++;
                }
            }
            bottom++;
            
            for(int i = right; i>=left; i--){
                if(i >= 0 && i < cols && bottom < rows){
                    ans.push_back({bottom,i});
                    count++;
                }
            }
            left--;
            
            for(int i = bottom; i>=top; i--){
                if(i >= 0 && i < rows && left >= 0){
                    ans.push_back({i,left});
                    count++;
                }
            }
            top--;
        }
        return ans;
    }
};