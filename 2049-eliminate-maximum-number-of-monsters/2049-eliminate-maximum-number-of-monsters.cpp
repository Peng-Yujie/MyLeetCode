class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        vector<int> time;
        for (int i=0; i < n; i++){
            time.push_back((dist[i]-1)/speed[i]);
        }
        sort(time.begin(),time.end());
        for (int i=0; i < n; i++){
            if (i > time[i]){
                return i;
            }
        }
        return n;
    }
};