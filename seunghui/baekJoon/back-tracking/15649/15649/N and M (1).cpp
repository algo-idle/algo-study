#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	for (int i = 1; i <= n; i++) {
		if (!isused[i]) {
			arr[k] = i;
			isused[i] = true;
			back_tracking(k + 1);
			isused[i] = false;
		}
	}
}

int main(void) {

	std::cin >> n >> m;
	back_tracking(0);

	return 0;
}