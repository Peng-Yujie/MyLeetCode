class MyHashMap {
public:
    vector<vector<int>> m;
    MyHashMap() {
        
    }
    
    void put(int key, int value) {
        int flag = 0;
        for(int i = 0; i < m.size(); i++){
            if(m[i][0] == key){
                flag = 1;
                m[i][1] = value;
            }
        }
        if(flag == 0){
            vector<int> temp;
            temp.push_back(key);
            temp.push_back(value);
            m.push_back(temp);
        }
    }
    
    int get(int key) {
        for(int i = 0; i < m.size(); i++){
            if(m[i][0] == key){
                return m[i][1];
            }
        }
        return -1;
    }
    
    void remove(int key) {
        for(int i = 0; i < m.size(); i++){
            if(m[i][0] == key){
                m[i][1] = -1;
                break;
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */