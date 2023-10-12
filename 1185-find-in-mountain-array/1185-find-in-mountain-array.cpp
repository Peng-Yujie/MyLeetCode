/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        // find the peak
        int index1 = -1, index2 = -1;
        int l = 0, r = mountainArr.length()-1;
        int mid = l + (r-l)/2;
        while(l<r){
            if(mountainArr.get(mid) < mountainArr.get(mid+1)){
                l = mid + 1;
            } else {
                r = mid;
            }
            mid = l + (r-l)/2;
        }
        int peak = mid;
        l = 0;
        r = peak;
        while(l <= r){
            mid = l + (r-l)/2;
            int t1 = mountainArr.get(mid);
            if (t1 == target){
                index1 = mid;
                break;
            } else if (t1 < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        l = peak + 1;
        r = mountainArr.length() - 1;
        while(l <= r){
            mid = l + (r-l)/2;
            int t2 = mountainArr.get(mid);
            if (t2 == target){
                index2 = mid;
                break;
            } else if (t2 > target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return index1 != -1 ? index1 : index2;
    }
};