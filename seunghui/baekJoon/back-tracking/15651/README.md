# 15651번: N과 M (3)

## 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

## 문제 설명
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/fb00a2bb-970f-465c-9f33-6c4bff9d6aa6)

### Example 2:     
![image](https://github.com/user-attachments/assets/80a29c41-7bec-4321-817e-310bf55af749)

### Example 3:     
![image](https://github.com/user-attachments/assets/373e4412-a600-4fd4-85bf-a3d6cc64593a)

# 코드 1
```cpp
#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking3(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		for (int i = 1; i <= n; i++) {
			arr[k] = i;
			back_tracking3(k + 1);
		}
	}
}

int main(void) {
	std::cin >> n >> m;
	back_tracking3(0);
	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/96d8f1fd-4139-469d-afc9-cdd40ec4c91a)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
