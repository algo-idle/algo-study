# 66번: Plus One

## 문제
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

## 문제 설명
큰 수를 자릿수 별로 나눈 배열이 주어진다. 1을 더했을 때의 결과 값을 배열로 출력하라.

## 예시
### Example 1:
Input: digits = [1,2,3]  
Output: [1,2,4]  
Explanation: The array represents the integer 123.  
Incrementing by one gives 123 + 1 = 124.  
Thus, the result should be [1,2,4].  

### Example 2:
Input: digits = [4,3,2,1]  
Output: [4,3,2,2]  
Explanation: The array represents the integer 4321.  
Incrementing by one gives 4321 + 1 = 4322.  
Thus, the result should be [4,3,2,2].  

### Example 3:
Input: digits = [9]  
Output: [1,0]  
Explanation: The array represents the integer 9.  
Incrementing by one gives 9 + 1 = 10.  
Thus, the result should be [1,0].  

## 코드
```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digit) {
        int size = digit.size();
        digit[size - 1] += 1;

        for (int i = 0; i < size; i++) {
            if (size == 1) {
                if (digit[i] == 10) {
                    digit[size - 1] = 1;
                    digit.push_back(0);
                }
            }
            if (digit[size - (i + 1)] == 10) {
                if (size - (i + 2) < 0) {
                    digit[size - (i + 1)] = 1;
                    digit.push_back(0);
                }
                else {
                    digit[size - (i + 1)] = 0;
                    digit[size - (i + 2)] += 1;
                }
            }
        }

        for (int i = 0; i < digit.size(); i++) {
            cout << digit[i];
        }

        return digit;
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/bd326e34-1dc1-471d-aa08-1f487dcaef8e)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/4af5c21d-1a01-41fb-b813-3e38146a7577)
