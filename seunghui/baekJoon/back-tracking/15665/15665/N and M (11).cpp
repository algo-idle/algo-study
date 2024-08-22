#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };

void back_tracking12(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		// ������ ����� ���ڸ� �����ϴ� ����
		int last_used = -1;
		for (int i = 0; i < n; i++) {
			if (k >= 1 && arr[k - 1] > nums[i]) {
				continue;
			}
			if (nums[i] != last_used) {
				arr[k] = nums[i];
				// �������� ����� ���ڸ� ���
				last_used = nums[i];
				back_tracking12(k + 1);
			}
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
	back_tracking12(0);
	return 0;
}