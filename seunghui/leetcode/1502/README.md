# 1502번: Can Make Arithmetic Progression From Sequence

## 문제
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

## 문제 설명
배열 요소들의 차이가 일정하면 true 아니면 false를 출력하라.

## 예시
### Example 1:  
Input: arr = [3,5,1]    
Output: true    
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.    

### Example 2:     
Input: arr = [1,2,4]    
Output: false    
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.    

## 코드
```cpp
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        for (int i = 0; i < arr.size() - 1; i++) {
            int min_idx = i;
            for (int j = i + 1; j < arr.size(); j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            std::swap(arr[min_idx], arr[i]);
        }

        int dif = arr[1] - arr[0];
        for (int i = 1; i < arr.size() - 1; i++){
            if (arr[i+1]-arr[i] != dif){
                return false;
            }
        }
        return true;
    }
};
```

## 채점 결과
![스크린샷 2024-07-04 175448](https://github.com/algo-idle/algo-study/assets/92175769/8d943c63-63db-45dd-bf2d-b182618c9931)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/f14a1127-a8df-4036-9177-e293dfed2e5b)

