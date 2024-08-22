# 15650번: N과 M (2)

## 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

## 문제 설명
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/8edff04b-a604-43ca-98bd-cf8f488f5a84)

### Example 2:     
![image](https://github.com/user-attachments/assets/051bcc58-785d-4071-86ce-0a6dd5f55a27)

### Example 3:     
![image](https://github.com/user-attachments/assets/572ad078-c13d-4de0-a8f7-d048de1f780b)

# 코드 1
```cpp
#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking2(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	for (int i = 1; i <= n; i++) {
		if (!isused[i]) {
			if (k >= 1 && arr[k - 1] > i) {
				continue;
			}
			arr[k] = i;
			isused[i] = true;
			back_tracking2(k + 1);
			isused[i] = false;
		}
	}
}

int main(void) {
	std::cin >> n >> m;
	back_tracking2(0);
	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/8246b6c5-3650-4ce6-b401-98c2cb69c1d0)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
