#include <iostream>
#include <vector>

int n;
std::vector<std::vector<int>> chessboard;

bool isused1[40] = { false, };
bool isused2[40] = { false, };
bool isused3[40] = { false, };

int cnt = 0;

//cur번째 행에 퀸을 배치할 예정
void func(int cur) {
	//퀸 n개를 다 놨음 -> cnt++
	if (cur == n) {
		cnt++;
		return;
	}

	for (int i = 0; i < n; i++) {
		if (!isused1[i] && !isused2[cur + i] && !isused3[cur - i + n - 1]) {
			isused1[i] = true;
			isused2[cur + i] = true;
			isused3[cur - i + n - 1] = true;
			
			func(cur + 1);

			isused1[i] = false;
			isused2[cur + i] = false;
			isused3[cur - i + n - 1] = false;
		}
	}
}

int main(void) {
	std::cin >> n;
	func(0);

	std::cout << cnt;
	return 0;
}