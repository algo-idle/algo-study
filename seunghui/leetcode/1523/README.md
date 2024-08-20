# 1523번: Count Odd Numbers in an Interval Range

## 문제
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

## 문제 설명
주어진 low와 high 사이의 홀수의 개수를 구하

## 예시
### Example 1:  
Input: low = 3, high = 7  
Output: 3  
Explanation: The odd numbers between 3 and 7 are [3,5,7].

### Example 2:     
Input: low = 8, high = 10  
Output: 1  
Explanation: The odd numbers between 8 and 10 are [9]. 

## 코드
```cpp
class Solution {
public:
    int countOdds(int low, int high) {
        int cnt = 0;
        for (int i = low; i <= high; i++){
            if (i % 2 != 0){
                cnt++;
            }
        }
        return cnt;
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/57a48f9a-a667-4060-8718-8cfd51d68ed1)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/57e68176-ac27-42fd-b5f7-343acc2f8a3c)

오늘은 양심없게 갔슴다.. 하나 더 풀어 올려야디..
