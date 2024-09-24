#include <iostream>
#include <vector>
#include <queue>

// ���μ���
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

    int maxSize = 0;  // ���� ū �׸� ũ��
    int count = 0;    // �׸� ����

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (pic[i][j] == 1 && !isVisited[i][j]) {
                // ���ο� �׸��� �߰������Ƿ� BFS ����
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

                // �׸� ũ�� ��
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
