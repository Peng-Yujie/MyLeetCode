class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        int count = 0;
        vector<vector<int>> ans;
        int left = cStart, right = cStart, top = rStart, bottom = rStart;
        while (count < rows*cols){
            
            for(int i = left; i <= right; i++){
                if (i>=0 && i < cols && top >=0 && top < rows){
                    vector<int> item;
                    item.push_back(top);
                    item.push_back(i);
                    ans.push_back(item);
                    count++;
                }
            }
right++;
            
            for(int i = top; i<= bottom; i++){
                if (i>=0 && i < rows && right >= 0 && right < cols){
                    vector<int> item;
                    item.push_back(i);
                    item.push_back(right);
                    ans.push_back(item);
                    count++;
                }
            }
bottom++;
            
            for(int i = right; i>=left; i--){
                if(i>=0 && i<cols && bottom >= 0 && bottom < rows){
                    vector<int> item;
                    item.push_back(bottom);
                    item.push_back(i);
                    ans.push_back(item);
                    count++;
                }
            }
left--;
            
            for(int i = bottom; i>=top; i--){
                if(i>=0 && i<rows && left >=0 && left < cols){
                    vector<int> item;
                    item.push_back(i);
                    item.push_back(left);
                    ans.push_back(item);
                    count++;
                }
            }
            top--;
        }
        return ans;
    }
};