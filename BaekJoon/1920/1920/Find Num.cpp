#include <iostream>
#include <vector>
#include <algorithm>

int main(void) {
    int t;
    std::cin >> t;

    std::vector<int> nums;
    while (t--) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    std::sort(nums.begin(), nums.end());

    int t2;
    std::cin >> t2;

    std::vector<int> check(t2, 0);
    int k = 0;
    while (t2--) {
        int num2;
        std::cin >> num2;

        int start = 0;
        int end = nums.size() - 1;
        while (start <= end) {
            int mid = (start + end) / 2; 

            if (num2 < nums[mid]) {
                end = mid - 1;
            }
            else if (num2 > nums[mid]) {
                start = mid + 1;
            }
            else {
                check[k] = 1;
                break;
            }
        }
        k++;
    }

    for (int i = 0; i < check.size(); i++) {
        std::cout << check[i] << "\n";
    }
    return 0;
}
