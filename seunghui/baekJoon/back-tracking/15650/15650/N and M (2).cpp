#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking2(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	for (int i = 1; i <= n; i++) {
		if (!isused[i]) {
			if (k >= 1 && arr[k - 1] > i) {
				//반복문 끝으로 가야 함
				//break 반복문 탈출해서 안됨
				continue;
			}
			arr[k] = i;
			isused[i] = true;
			back_tracking2(k + 1);
			isused[i] = false;
		}
	}
}

int main(void) {
	std::cin >> n >> m;
	back_tracking2(0);
	return 0;
}