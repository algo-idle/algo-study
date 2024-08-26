#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking4(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		for (int i = 1; i <= n; i++) {
			if (k >= 1 && arr[k - 1] > i) {
				continue;
			}
			arr[k] = i;
			back_tracking4(k + 1);
		}
	}
}

int main(void) {
	std::cin >> n >> m;
	back_tracking4(0);
	return 0;
}