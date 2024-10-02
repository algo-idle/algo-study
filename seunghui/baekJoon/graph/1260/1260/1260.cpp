#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

std::vector<int> matrix[1001];
bool isvisited_dfs[1001] = { false, };
bool isvisited_bfs[1001] = { false, };

//dfs
std::stack<int> s;
void dfs(int v) {
	if (!isvisited_dfs[v]) {
		s.push(v);
		std::cout << s.top() <<" ";
		s.pop();
		isvisited_dfs[v] = true;

		for (auto next : matrix[v]) {
			if (!isvisited_dfs[next]) {
				dfs(next);
			}
		}
	}
}

//bfs
std::queue<int> q;
void bfs(int v) {
	if (!isvisited_bfs[v]) {
		q.push(v);
		isvisited_bfs[v] = true;

		while (!q.empty()) {
			int cur = q.front();
			std::cout << cur << " ";
			q.pop();

			for (auto next : matrix[cur]) {
				if (!isvisited_bfs[next]) {
					q.push(next);
					isvisited_bfs[next] = true;
				}
			}			
		}
	}
}

int main(void) {
	//정점의 개수 n, 간선의 개수 m, 시작 정점의 번호 v
	int n, m, v;
	std::cin >> n >> m >> v;

	while (m--) {
		int v1, v2;
		std::cin >> v1 >> v2;
		matrix[v1].push_back(v2);
		matrix[v2].push_back(v1);
	}

	for (int i = 1; i <= n; i++) {
		std::sort(matrix[i].begin(), matrix[i].end());
	}	

	dfs(v);
	std::cout << "\n";
	bfs(v);

	return 0;
}