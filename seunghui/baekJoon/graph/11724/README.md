# 11724번: 연결 요소의 개수

## 문제

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

## 문제 설명

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

첫째 줄에 연결 요소의 개수를 출력한다.

## 예시

### Example 1:

![스크린샷 2024-10-02 213842](https://github.com/user-attachments/assets/f9488c0b-21c8-4b3c-b588-b30c884dd179)


### Example 2:

![스크린샷 2024-10-02 213902](https://github.com/user-attachments/assets/a4273cb0-bb31-4ae1-983c-3dfce2cf0313)


# 코드

```cpp
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
```

## 채점 결과

![스크린샷 2024-10-02 213941](https://github.com/user-attachments/assets/97f6cc44-3123-44e5-bb99-843bc9979b14)


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)

![스크린샷 2024-10-02 214017](https://github.com/user-attachments/assets/e28e2139-1dff-4bf5-8414-dc71409bf611)
