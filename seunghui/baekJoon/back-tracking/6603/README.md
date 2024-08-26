# 6603번: 로

## 문제
독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.

로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

## 문제 설명
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다. 

각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/7dd50fe5-ec32-4c69-a631-04779f7a4960)

# 코드 1
```cpp
#include <iostream>
#include <vector>

int k0;
std::vector<int> s(0);

int arr[10] = { 0, };
int isused[50] = { false, };

void lotto(int k) {
	if (k == 6) {
		for (int i = 0; i < 6; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	
	for (int i : s) {
		if (!isused[i]) {
			if (k >= 1 && arr[k - 1] > i) {
				continue;
			}
			arr[k] = i;
			isused[i] = true;
			lotto(k + 1);
			isused[i] = false;
		}
	}
}

int main(void) {
	while (true) {
		std::cin >> k0;
		if (k0 == 0) {
			break;
		}

		s.resize(k0);
		for (int i = 0; i < k0; i++) {
			std::cin >> s[i];
		}

		lotto(0);
		std::cout << "\n";
	}

	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/9fbac086-de48-42c3-953e-d3fdde599ac5)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/995a25d6-61bc-4c2e-8457-2bba41a25830)
