# 1920번: 수 찾기

## 문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

## 문제 설명
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.  
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/9c708188-0cd1-4e0d-8b31-f833dad8ef33)

# 코드 1
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main(void) {
    int t;
    std::cin >> t;

    std::vector<int> nums;
    while (t--) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    std::sort(nums.begin(), nums.end());

    int t2;
    std::cin >> t2;

    std::vector<int> check(t2, 0);
    int k = 0;
    while (t2--) {
        int num2;
        std::cin >> num2;

        int start = 0;
        int end = nums.size() - 1;
        while (start <= end) {
            int mid = (start + end) / 2; 

            if (num2 < nums[mid]) {
                end = mid - 1;
            }
            else if (num2 > nums[mid]) {
                start = mid + 1;
            }
            else {
                check[k] = 1;
                break;
            }
        }
        k++;
    }

    for (int i = 0; i < check.size(); i++) {
        std::cout << check[i] << "\n";
    }
    return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/eef7dd68-2338-456a-be0d-0b21ffabd40c)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/53f3b9f6-d3c3-41ce-8db5-75f95b580a29)

