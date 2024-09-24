# 네트워크

## 문제 설명

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

## 제한 사항

- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 `n-1`인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

## 예시

### Example 1:

![스크린샷 2024-09-25 014658](https://github.com/user-attachments/assets/458e556f-d98f-4162-9252-7646aabc1c43)


# 코드

```cpp
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> isvisited(n, 0);
    
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    queue<int> q;
    int cnt = 0;
    for (int i = 0; i < n; i++){
        if (!isvisited[i]){
            q.push(i);
            isvisited[i] = true;

            while (!q.empty()){
                int cur = q.front();
                q.pop();

                for (int k = 0; k < n; k++){
                    if (!isvisited[k] && computers[cur][k] == 1){
                        q.push(k);
                        isvisited[k] = true;
                    }
                }
            }
            cnt++;
        }
    }
    answer = cnt;
    return answer;
}
```

## 채점 결과

![스크린샷 2024-09-25 014735](https://github.com/user-attachments/assets/42e8c91d-6fdb-482a-8d35-c9cc5bdcfd07)


## 어떻게 풀었는지..

처음에 문제를 잘못 이해해서 좌표 탐색 방식으로 풀었다가 틀렸었음

그래서 다시 문제를 보고 이해한 뒤 인덱스 간의 관계를 고려하여 풀었음

1. 각 컴퓨터가 연결된 다른 컴퓨터들을 찾아 **네트워크의 일부**로 묶고, 그 연결된 컴퓨터들을 모두 방문 처리 한다.
2. 각  컴퓨터가 네트워크에 속해있는지 여부를 isvisited 배열로 관리한다.
3. 네트워크를 확인할 때는 computers[i][j] == 1 인지 확인하고, 상하좌우 탐색이 아니라 각 컴퓨터의 인덱스 관계를 살펴본다.
