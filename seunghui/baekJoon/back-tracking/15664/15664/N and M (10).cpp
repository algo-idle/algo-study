#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };
int isused[10001] = { false, };

void back_tracking10(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	// 이전에 사용한 숫자를 저장하는 변수
	int last_used = -1;
	for (int i = 0; i < n; i++) {
		if (k >= 1 && arr[k - 1] > nums[i]) {
			continue;
		}

		if (!isused[i] && nums[i] != last_used) {
			arr[k] = nums[i];
			isused[i] = true;
			// 마지막에 사용한 숫자를 기록
			last_used = nums[i];
			back_tracking10(k + 1);
			isused[i] = false;
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
	back_tracking10(0);
	return 0;
}