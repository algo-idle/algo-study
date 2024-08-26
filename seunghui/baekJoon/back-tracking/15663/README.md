# 15663번: N과 M (9)

## 문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열

## 문제 설명
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/d4b8468c-bde3-45e7-83e9-77826075bc47)

### Example 2:     
![image](https://github.com/user-attachments/assets/1859b338-6e35-4f3e-b5ae-acfec78abd2f)

### Example 3:     
![image](https://github.com/user-attachments/assets/842856b1-8813-4537-8776-ae39494af432)

# 코드 1
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };
int isused[10001] = { false, };

void back_tracking9(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}
	
	// 이전에 사용한 숫자를 저장하는 변수
	int last_used = -1;
	for (int i = 0; i < n; i++) {
		if (!isused[i] && nums[i] != last_used) {
			arr[k] = nums[i];
			isused[i] = true;
			// 마지막에 사용한 숫자를 기록
			last_used = nums[i]; 
			back_tracking9(k + 1);
			isused[i] = false;
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
	back_tracking9(0);
	return 0;
}
```

## 채점 결과
처음에 벡터에서 중복 요소를 없애려고 set을 시도해봤는데, 그렇게 풀면 아예 배열에서 중복된 요소가 사라지기 때문에 예제에서의 9 9 또는 1 1 1 1 과 같은 답이 나오지 않는다.  
그래서 이전에 사용한 숫자를 저장하는 변수를 사용하여 문제를 풀었다. 
![image](https://github.com/user-attachments/assets/57d3054b-5c4b-479b-8711-adc22fe47489)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
