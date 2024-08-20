#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int arraySign(vector<int>& nums) {
        int negative_cnt = 0;
        int positive_cnt = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                return 0;
            }
            if (nums[i] < 0) {
                negative_cnt++;
            }
        }

        if (negative_cnt % 2 == 0) {
            return 1;
        }
        else {
            return -1;
        }
    }
};

int main(void) {
    //페이지에서 바로 풀음
    return 0;
}