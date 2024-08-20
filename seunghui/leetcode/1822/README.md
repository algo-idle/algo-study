# 1822번: Sign of the Product of an Array

## 문제
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

## 문제 설명
배열 안의 숫자를 곱하여 양수면 1, 음수면 -1, 0이면 0을 출력하라.

## 예시
### Example 1:  
Input: nums = [-1,-2,-3,-4,3,2,1]  
Output: 1  
Explanation: The product of all values in the array is 144, and signFunc(144) = 1    

### Example 2:     
Input: nums = [1,5,0,2,-3]  
Output: 0  
Explanation: The product of all values in the array is 0, and signFunc(0) = 0  

### Example 3:   
Input: nums = [-1,1,-1,1,-1]  
Output: -1  
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1  

## 코드
```cpp
class Solution {
public:
    int arraySign(vector<int>& nums) {
        int negative_cnt = 0;
        int positive_cnt = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 0){
                return 0;
            }
            if (nums[i] < 0){
                negative_cnt++;
            }
        }

        if (negative_cnt % 2 == 0){
            return 1;
        }
        else{
            return -1;
        }
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/7d7ef05a-774a-4ba0-8b72-3b25a004c534)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/878a9454-464d-478e-b7b8-beb5802ba7f6)

풀다 만 문제길래 어려운 줄 알고 풀었는데 꽤나 쉽게 풀렸다   
그래서 왜 풀다 말았나 생각해보니 그냥 냅다 곱하고 범위초과로 두번이나 틀려서 스트레스 받아서 그냥 안했던 ..  
그냥 음수의 개수만 구하면 됐던 것을!!
