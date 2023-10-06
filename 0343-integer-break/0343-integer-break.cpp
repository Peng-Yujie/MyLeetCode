class Solution {
public:
    int integerBreak(int n) {
        if (n<=3){
            return n-1;
        }
        int res = 1;
        int quotient = n/3, remainder = n%3;
        if (remainder == 0){
            res = pow(3, quotient);
        } else if (remainder == 1){
            res = pow(3, quotient-1) * 4;
        } else {
            res = pow(3, quotient) * 2;
        }
        return res;
    }
};