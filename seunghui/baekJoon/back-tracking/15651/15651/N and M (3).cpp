#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking3(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		for (int i = 1; i <= n; i++) {
			arr[k] = i;
			back_tracking3(k + 1);
		}
	}
}

int main(void) {
	std::cin >> n >> m;
	back_tracking3(0);
	return 0;
}