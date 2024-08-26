#include <vector>
#include <queue>
using namespace std;

int solution(vector<vector<int>> maps)
{
  int answer = 0;
  int dx[4] = {0, 0, 1, -1};
  int dy[4] = {1, -1, 0, 0};
  int n = maps.size();    // 행
  int m = maps[0].size(); // 열

  vector<vector<int>> dist(n, vector<int>(m, -1)); // -1은 방문하지 않은 곳
  queue<pair<int, int>> q;
  q.push({0, 0}); // 시작점
  dist[0][0] = 1; //  시작 거리

  while (!q.empty())
  {
    int x = q.front().first;
    int y = q.front().second;
    q.pop(); // 현재위치를 꺼냄

    for (int i = 0; i < 4; i++)
    {
      // 다음위치
      int nx = x + dx[i];
      int ny = y + dy[i];

      // 맵 범위를 벗어남
      if (nx < 0 || nx >= n || ny < 0 || ny >= m)
        continue;
      // 이동불가
      if (maps[nx][ny] == 0)
        continue;
      // 이미 방문한 곳
      if (dist[nx][ny] != -1)
        continue;

      // 최단거리 갱신
      dist[nx][ny] = dist[x][y] + 1;
      q.push({nx, ny});
    }
  }

  answer = dist[n - 1][m - 1];

  return answer;
}