# 976번: Largest Perimeter Triangle

## 문제
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

## 문제 설명
삼각형의 조건에 맞는 3개의 변의 조합 중에 그의 합이 최대인 것을 출력하라.

## 예시
### Example 1:  
Input: nums = [2,1,2]  
Output: 5  
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

### Example 2:     
Input: nums = [1,2,1,10]  
Output: 0  
Explanation:   
You cannot use the side lengths 1, 1, and 2 to form a triangle.  
You cannot use the side lengths 1, 1, and 10 to form a triangle.  
You cannot use the side lengths 1, 2, and 10 to form a triangle.  
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.

## 코드
```cpp
#include <iostream>

class Solution {
public:
    int largestPerimeter(vector<int>& nums) {
       vector<int> triangle;
       sort(nums.begin(), nums.end(), greater<int>());

       int k = 0;
       for (int i = 1; i < nums.size()-1; i++) {
            if (nums[k] < nums[i] + nums[i+1]){
                triangle.push_back(nums[k] + nums[i] + nums[i+1]);
            }
            k++;
       }

       int max = 0;
       for (int i = 0; i < triangle.size(); i++){
            if (triangle[i] >= max){
                max = triangle[i];
            }
       }

       return max;
    }
};
```

## 채점 결과
![image](https://github.com/user-attachments/assets/78b1f003-2501-4c65-8fb8-afbc90be41b3)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/44c85138-40e1-4ea0-9dd7-18dde9089e53)

삼각형의 조건인 "제일 긴 변의 길이 < 나머지 두 변의 길이의 합" 을 이용했다.  
