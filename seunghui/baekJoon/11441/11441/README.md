# 11441번: 합 구하기

## 문제
N개의 수 A1, A2, ..., AN이 입력으로 주어진다. 총 M개의 구간 i, j가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

## 문제 설명
첫째 줄에 수의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 둘째 줄에는 A1, A2, ..., AN이 주어진다. (-1,000 ≤ Ai ≤ 1,000) 셋째 줄에는 구간의 개수 M이 주어진다. (1 ≤ M ≤ 100,000) 넷째 줄부터 M개의 줄에는 각 구간을 나타내는 i와 j가 주어진다. (1 ≤ i ≤ j ≤ N)

총 M개의 줄에 걸쳐 입력으로 주어진 구간의 합을 출력한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/8cb1a2f2-2fd5-4934-8e69-e39fc6593d7d)

### Example 2:  
![image](https://github.com/user-attachments/assets/d6c43553-aa56-47a4-926b-2895fe944713)

# 코드 1
```cpp
#include <iostream>
#include <vector>

int main(void) {
	int n;
	std::cin >> n;
	
	std::vector<int> nums;
	while (n--) {
		int num;
		std::cin >> num;
		nums.push_back(num);
	}

	int m;
	std::cin >> m;
	while (m--) {
		int a, b;
		std::cin >> a >> b;

		int sum = 0;
		for (int i = a - 1; i <= b - 1; i++) {
			sum += nums[i];
		}
		std::cout << sum << "\n";
	}
	return 0;
}
```
시간 초과 뜸
그래서 시간 복잡도를 분석해봄

벡터 'nums'에 입력을 받을 때의 시간 복잡도는 'O(n)'
구간 'a'에서 'b'까지의 합을 구하는데, 이 경우 'O(b - a + 1)'
최악의 경우 구간이 전체 배열에 해당할 경우 'O(n)'
구간이 m개가 주어지게 된다면, 시간 복잡도는 'O(m * n)'

즉, n과 m이 충분히 큰 경우 시간 초가가 발생할 수 있음

예를 들어
1. n = 100,000
2. m = 100,000
3. 모든 m개의 구간이 배열 전체의 합을 구하는 경우

이 예시에서의 시간 복잡도는 'O(n * m) = O(10^10)'이 됨
따라서, 1초 이내로 해결할 수 없게 됨

위와 같은 이유로 시간 초과가 떴고, 그렇기 때문에 해결 방법을 알아본 결과 "누적 합" 이라는 알고리즘을 썼음

# 코드 2
```cpp
#include <iostream>
#include <vector>

int main(void) {
	int n;
	std::cin >> n;
	
	std::vector<int> nums;
	while (n--) {
		int num;
		std::cin >> num;
		nums.push_back(num);
	}

	int m;
	std::cin >> m;
	while (m--) {
		int a, b;
		std::cin >> a >> b;

		int sum = 0;
		for (int i = a - 1; i <= b - 1; i++) {
			sum += nums[i];
		}
		std::cout << sum << "\n";
	}
	return 0;
}
```
누적 합 알고리즘을 썼음에도 불구하고 시간 초과가 떴다.

그래서 마지막으로 cin과 cout의 동기화를 비활성화했다.	

해결됐다.	

# 코드 3
```cpp
#include <iostream>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL); 

    int n;
    std::cin >> n;

    std::vector<int> nums(n + 1, 0); 
    for (int i = 1; i <= n; i++) {
        int num;
        std::cin >> num;

        // 누적 합 계산
        nums[i] = nums[i - 1] + num; 
    }

    int m;
    std::cin >> m;
    while (m--) {
        int a, b;
        std::cin >> a >> b;

        // 구간 합 계산
        std::cout << nums[b] - nums[a - 1] << "\n"; 
    }

    return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/2d58fdca-3873-499f-ab61-01a12a9763c0)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/b3ebd263-a425-4431-8b9a-fec7f83e1e1f)

12시 지나고 풀어서 공백 발생
