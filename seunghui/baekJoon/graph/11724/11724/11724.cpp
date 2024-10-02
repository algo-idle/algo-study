#include <iostream>
#include <vector>
#include <queue>

int main(void) {
	int n, m;
	std::cin >> n >> m;

	std::vector<std::vector<int>> g(1001, std::vector<int>(1001, 0));
	bool isvisited[1001] = { false, };

	// 그래프 입력
	while (m--) {
		int u, v;
		std::cin >> u >> v;
		g[u].push_back(v);
		g[v].push_back(u);
	}

	// BFS
	int num = 0;
	for (int i = 1; i <= n; i++) {
		if (!isvisited[i]) {
			std::queue<int> q;
			q.push(i);
			isvisited[i] = true;

			while (!q.empty()) {
				int cur = q.front();
				q.pop();

				for (auto next : g[cur]) {
					if (!isvisited[next]) {
						q.push(next);
						isvisited[next] = true;
					}
				}
			}
			num++;
		}
	}

	std::cout << num;

	return 0;
}