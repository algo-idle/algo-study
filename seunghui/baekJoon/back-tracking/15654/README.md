# 15654번: N과 M (5)

## 문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열

## 문제 설명
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/e5b3fa8f-f5fa-4eef-8e7d-b47c40f87578)

### Example 2:     
![image](https://github.com/user-attachments/assets/e4314803-de49-4870-8539-affdd6193918)

### Example 3:     
![image](https://github.com/user-attachments/assets/c3ce4a4f-86d5-4baa-b4c7-126038a5685d)

# 코드 1
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int n, m;
std::vector<int> nums;
int arr[10] = { 0, };
bool isused[10001] = { false, };

void back_tracking5(int k) {
	if (k == m) {
		for (int i = 0; i < m; i++) {
			std::cout << arr[i] << " ";
		}
		std::cout << "\n";
	}

	for (int i : nums) {
		if (!isused[i]) {
			arr[k] = i;
			isused[i] = true;
			back_tracking5(k + 1);
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
	back_tracking5(0);
	return 0;
}
```

## 채점 결과
처음에 isused 배열의 크기를 10에서 100001으로 늘리지 않아 배열 크기 오류가 났었고, 그걸 수정한 결과 맞았다.  
다음에 문제 풀때 배열의 크기를 좀 더 주의해서 보도록 하겠다.
![image](https://github.com/user-attachments/assets/8b80e11d-6e2b-4671-9c6e-8d53757ae6da)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/8fc3f14d-fd27-4143-bef6-da8e1256cc3f)
