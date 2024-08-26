#include <iostream>
#include <vector>

int k0;
std::vector<int> s(0);

int arr[10] = { 0, };
int isused[50] = { false, };

void lotto(int k) {
	if (k == 6) {
		for (int i = 0; i < 6; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	
	for (int i : s) {
		if (!isused[i]) {
			if (k >= 1 && arr[k - 1] > i) {
				continue;
			}
			arr[k] = i;
			isused[i] = true;
			lotto(k + 1);
			isused[i] = false;
		}
	}
}

int main(void) {
	while (true) {
		std::cin >> k0;
		if (k0 == 0) {
			break;
		}

		s.resize(k0);
		for (int i = 0; i < k0; i++) {
			std::cin >> s[i];
		}

		lotto(0);
		std::cout << "\n";
	}

	return 0;
}