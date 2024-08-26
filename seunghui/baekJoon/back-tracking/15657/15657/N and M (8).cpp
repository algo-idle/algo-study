#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };

void back_tracking8(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		for (int i : nums) {
			if (k >= 1 && arr[k - 1] > i) {
				continue;
			}
			arr[k] = i;
			back_tracking8(k + 1);
		}
	}
}

int main(void) {
	std::cin >> n >> m;

	for (int i = 0; i < n; i++) {
		int num;
		std::cin >> num;
		nums.push_back(num);
	}

	std::sort(nums.begin(), nums.end());
	back_tracking8(0);
	return 0;
}