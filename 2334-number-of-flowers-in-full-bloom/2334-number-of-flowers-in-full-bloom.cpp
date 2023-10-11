class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        vector<int> ans, start, end;
        // Find the start time and the end time of each flower
        for(auto i : flowers){
            start.push_back(i[0]);
            end.push_back(i[1]);
        }
        // Sort the start and end times
        sort(start.begin(),start.end());
        sort(end.begin(),end.end());
        
        for(int time : people){
            // At the moment, how many flowers have been in bloom
            int starts = upper_bound(start.begin(),start.end(),time) - start.begin();
            // At the moment, how many flowers end
            int ends = lower_bound(end.begin(),end.end(),time) - end.begin();
            ans.push_back(starts-ends);
        }
        return ans;


        // unordered_map<int,int> m;
        // for(int i = 0; i < flowers.size(); i++){
        //     for(int j= flowers[i][0]; j<= flowers[i][1]; j++){
        //         if(m.find(j) == m.end()){
        //             m.insert({j,1});
        //         } else {
        //             m.at(j)++;
        //         }
        //     }
        // }
        // for(int i = 0; i < people.size(); i++){
        //     int p = people[i];
        //     if(m.find(p) == m.end()){
        //         ans.push_back(0);
        //     } else {
        //         ans.push_back(m.at(p));
        //     }
        // }
    }
};