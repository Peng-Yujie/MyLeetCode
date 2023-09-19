class RandomizedSet {

private:
    vector<int> a;
    unordered_map<int, int> m;

public:
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        // check if val is present in the map or not
        if (m.find(val) != m.end()){
            return false;
        } else {
            // if not exist, add val to the end of the vector, and store the value and the index in the map
            a.push_back(val);
            m[val] = a.size() - 1;
            return true;
        }

    }
    
    bool remove(int val) {
        if (m.find(val) == m.end()){
            return false;
        } else {
            // Find the index of val in vector through map
            // Assign the value of last item to the current item, then delete the last item
            // Update the index in map, delete the duplicate one
            int last = a.back();
            a[m[val]] = last;
            a.pop_back();
            m[last] = m[val];
            m.erase(val);
            return true;
        }
    }
    
    int getRandom() {
        return a[rand()%a.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */