class Solution {
public:
    int minProcessingTime(vector<int>& processorTime, vector<int>& tasks) {
        sort(processorTime.begin(),processorTime.end());
        sort(tasks.rbegin(),tasks.rend());
        vector<int> takenTime;
        int maxTime = 0;
        for (int i = 0; i < processorTime.size(); i++){
            maxTime = max(maxTime, processorTime[i] + tasks[i*4]);
        }
        return maxTime;
    }
};