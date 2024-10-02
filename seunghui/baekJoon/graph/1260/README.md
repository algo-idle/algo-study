# 1260번: DFS와 BFS

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 문제 설명

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## 예시

### Example 1:

![스크린샷 2024-10-02 215550](https://github.com/user-attachments/assets/269a0eb6-cefb-4bb1-a35d-25e2303da77b)

### Example 2:

![스크린샷 2024-10-02 215605](https://github.com/user-attachments/assets/29fc70c1-8952-433b-9425-1863df9af537)

### Example 3:

![스크린샷 2024-10-02 215627](https://github.com/user-attachments/assets/563d819f-2d1f-4401-8152-a2534356e3e9)

# 코드

```cpp
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
```

## 채점 결과

![스크린샷 2024-10-02 215649](https://github.com/user-attachments/assets/7589340b-9a97-4838-91d8-65cbb4f04bdb)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)

![스크린샷 2024-10-02 214017](https://github.com/user-attachments/assets/4a304c38-8138-4aeb-9fe2-2eb02c548f85)
