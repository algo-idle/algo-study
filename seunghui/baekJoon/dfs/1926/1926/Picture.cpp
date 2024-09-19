#include <iostream>
#include <vector>
#include <stack>

int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int main(void) {
	int n, m;
	std::cin >> n >> m;

	std::vector<std::vector<int>> pic;
	std::vector<std::vector<bool>> isvisted;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int num;
			std::cin >> num;
			pic[i].push_back(num);
			isvisted[i].push_back(false);
		}
	}

	std::stack<std::pair<int, int>> s;
	isvisted[0][0] = true;
	
	s.push({ 0, 0 });

	int cnt = 0;
	while (!s.empty()) {
		std::pair<int, int> cur = s.top();
		s.pop();
		
		for (int i = 0; i < 4; i++) {
			int nx = cur.first + dx[i];
			int ny = cur.second + dy[i];

			if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
				continue;
			}

			if (isvisted[nx][ny] || pic[nx][ny] != 1) {
				continue;
			}
			else {
				cnt++;
			}

			isvisted[nx][ny] = true;
			s.push({ nx, ny });
		}
	}

	return 0;
}