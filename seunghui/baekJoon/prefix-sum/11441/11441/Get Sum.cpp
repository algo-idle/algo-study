#include <iostream>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL); 

    int n;
    std::cin >> n;

    std::vector<int> nums(n + 1, 0); 
    for (int i = 1; i <= n; i++) {
        int num;
        std::cin >> num;

        // 누적 합 계산
        nums[i] = nums[i - 1] + num; 
    }

    int m;
    std::cin >> m;
    while (m--) {
        int a, b;
        std::cin >> a >> b;

        // 구간 합 계산
        std::cout << nums[b] - nums[a - 1] << "\n"; 
    }

    return 0;
}
