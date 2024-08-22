#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };
//범위 오류 났었음 => 확인 제대로 할 것!
bool isused[10001] = { false, };

void back_tracking5(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	for (int i : nums) {
		if (!isused[i]) {
			arr[k] = i;
			isused[i] = true;
			back_tracking5(k + 1);
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
	back_tracking5(0);
	return 0;
}