# 15649번: N과 M (1)

## 문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

## 문제 설명
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/fa4d534e-2b45-4520-9383-0896c712b623)

### Example 2:     
![image](https://github.com/user-attachments/assets/37800d42-6007-4da9-aafa-bd16e1bd28ca)

### Example 3:     
![image](https://github.com/user-attachments/assets/dc672346-dc53-4829-9b20-04e268d4aaa0)

# 코드 1
```cpp
#include <iostream>

int n, m;
int arr[10] = { 0, };
bool isused[10] = { false, };

void back_tracking(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	for (int i = 1; i <= n; i++) {
		if (!isused[i]) {
			arr[k] = i;
			isused[i] = true;
			back_tracking(k + 1);
			isused[i] = false;
		}
	}
}

int main(void) {

	std::cin >> n >> m;
	back_tracking(0);

	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/7e1b1d5a-8315-4546-b7b5-4770f4ee3610)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
