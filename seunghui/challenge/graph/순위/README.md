# 순위

## 문제 설명

n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한 사항

- 선수의 수는 1명 이상 100명 이하입니다.
- 경기 결과는 1개 이상 4,500개 이하입니다.
- results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
- 모든 경기 결과에는 모순이 없습니다.

## 예시

### Example 1:

![스크린샷 2024-10-02 220227](https://github.com/user-attachments/assets/391ac0cf-2978-4cfb-8155-750a1e8db383)

# 코드

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    std::vector<std::vector<int>> matrix(n+1, std::vector<int> (n+1, 0));
    for (int i = 0; i < results.size(); i++){
        //이겼을 때 1로 초기화
        matrix[results[i][0]][results[i][1]] = 1;
        //졌을 때 -1로 초기화
        matrix[results[i][1]][results[i][0]] = -1;
    }
    
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n ;j++){
            std::cout << matrix[i][j] << " ";
        }
        std::cout << "\n";
    }
    std::cout << "\n";
    
   // 플로이드-와샬 알고리즘을 사용하여 간접 승패 관계 업데이트
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (matrix[i][j] == 0) {  // 직간접적으로 아직 연결이 안 된 경우
                    if (matrix[i][k] == 1 && matrix[k][j] == 1) {
                        matrix[i][j] = 1;  // i가 k를 이기고 k가 j를 이기면 i는 j를 이긴다
                    }
                    if (matrix[i][k] == -1 && matrix[k][j] == -1) {
                        matrix[i][j] = -1; // i가 k에게 지고 k가 j에게 지면 i는 j에게 진다
                    }
                }
            }
        }
    }
    
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n ;j++){
            std::cout << matrix[i][j] << " ";
        }
        std::cout << "\n";
    }
    
    int answer = 0;
    int cnt = 0;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j<= n; j++){
            if (matrix[i][j] == 0){
                cnt++;
            }
        }
        if (cnt == 1){
            answer++;
        }
        cnt = 0;
    }
    return answer;
}
```

## 실행 결과

![스크린샷 2024-10-02 222618](https://github.com/user-attachments/assets/28261cec-139d-4f3d-95b7-0d6cc229baaa)

## 어떻게 풀었는지..

플로이드-와샬 알고리즘의 경로 탐색 방식을 사용하여 문제를 해결하였음

플로이드-와샬 알고리즘에서의 경유지를 통해 경로를 업데이트하는 방식을, 이 문제에서 간접적인 승패 관계를 갱신하는데 응용되도록 하였음

즉, 승패 관계를 플로이드-와샬 알고리즘에 적용하였고, 

- 정점 : 각 정점은 1번부터 n번까지의 선수
- 간선 : 간선의 가중치는 승패 여부로, 1은 승리, -1은 패배로 정의함
- 경로 : 간선이 직접 연결되어 있지 않더라도, 중간 정점을 경유하여 간접적으로 연결될 수 있음
    - 3중 반복문 안의 조건문

정점, 간선, 경로를 위와 같이 생각하여 코드를 작성하였음
