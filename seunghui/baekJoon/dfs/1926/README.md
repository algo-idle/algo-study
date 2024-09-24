# 1926번: 그림

## 문제

어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

## 문제 설명

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

## 예시

### Example 1:

![스크린샷 2024-09-25 004923](https://github.com/user-attachments/assets/10fa9074-8a56-4e6a-a32f-bd7553f6797b)


# 코드

```cpp
#include <iostream>
#include <vector>
#include <queue>

// 가로세로
int dx[4] = { -1, 1, 0, 0 };
int dy[4] = { 0, 0, -1, 1 };

int main(void) {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<int>> pic(n, std::vector<int>(m, 0));
    std::vector<std::vector<bool>> isVisited(n, std::vector<bool>(m, false));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cin >> pic[i][j];
        }
    }

    int maxSize = 0;  // 가장 큰 그림 크기
    int count = 0;    // 그림 개수

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (pic[i][j] == 1 && !isVisited[i][j]) {
                // 새로운 그림을 발견했으므로 BFS 시작
                std::queue<std::pair<int, int>> q;
                q.push({ i, j });
                isVisited[i][j] = true;
                int width = 0;

                while (!q.empty()) {
                    auto cur = q.front();
                    q.pop();
                    width++;

                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.first + dx[dir];
                        int ny = cur.second + dy[dir];

                        if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
                            continue;
                        }
                        if (pic[nx][ny] == 1 && !isVisited[nx][ny]) {
                            q.push({ nx, ny });
                            isVisited[nx][ny] = true;
                        }
                    }
                }

                // 그림 크기 비교
                if (width > maxSize) {
                    maxSize = width;
                }
                count++;
            }
        }
    }

    std::cout << count << "\n" << maxSize;
    return 0;
}

```

## 채점 결과

![스크린샷 2024-09-25 004831](https://github.com/user-attachments/assets/1c576ae7-59be-4122-8a06-b46a45106aff)


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)

![스크린샷 2024-09-25 004941](https://github.com/user-attachments/assets/a945ae2e-9825-440d-8cc8-b162f8d7672d)


12시 50분에 제출하여 9월 25일로 찍힘
