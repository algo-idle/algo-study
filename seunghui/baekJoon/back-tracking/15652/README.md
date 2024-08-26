# 15652번: N과 M (4)

## 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- **같은 수를 여러 번 골라도 된다.**
- **고른 수열은 비내림차순이어야 한다.**
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

## 문제 설명
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/fb00a2bb-970f-465c-9f33-6c4bff9d6aa6)

### Example 2:     
![image](https://github.com/user-attachments/assets/496cabd7-fe3c-465c-84fe-cca365dff3d8)

### Example 3:     
![image](https://github.com/user-attachments/assets/75d054c7-311c-4d13-aa53-110e9c2657cf)

# 코드 1
```cpp
#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking4(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		for (int i = 1; i <= n; i++) {
			if (k >= 1 && arr[k - 1] > i) {
				continue;
			}
			arr[k] = i;
			back_tracking4(k + 1);
		}
	}
}

int main(void) {
	std::cin >> n >> m;
	back_tracking4(0);
	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/4567f2d3-9094-4027-a0ac-7c71b17cb75b)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
