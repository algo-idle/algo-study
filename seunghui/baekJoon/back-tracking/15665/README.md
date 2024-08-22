# 15665번: N과 M (11)

## 문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

## 문제 설명
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/d4b8468c-bde3-45e7-83e9-77826075bc47)

### Example 2:     
![image](https://github.com/user-attachments/assets/4eebd953-5e47-4e1f-9498-5773f3a91332)

### Example 3:     
![image](https://github.com/user-attachments/assets/5569abf7-0e41-4a6a-bd5d-94913119216f)

# 코드 1
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };

void back_tracking11(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	else {
		// 이전에 사용한 숫자를 저장하는 변수
		int last_used = -1;
		for (int i = 0; i < n; i++) {
			if (nums[i] != last_used) {
				arr[k] = nums[i];
				// 마지막에 사용한 숫자를 기록
				last_used = nums[i];
				back_tracking11(k + 1);
			}
		}
	}
}

int main(void) {
	std::cin >> n >> m;

	for (int i = 0; i < n; i++) {
		int num;
		std::cin >> num;
		nums.push_back(num);
	}

	std::sort(nums.begin(), nums.end());
	back_tracking11(0);
	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/fa2dc039-0cd7-4ccf-8bc3-667bae0fa254)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
