# Climbing Stairs

## 문제 설명
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## 예시

### Example 1:
![image](https://github.com/user-attachments/assets/3f49d54c-917b-4302-bf0d-901112dfa9a1)

### Example 2:
![image](https://github.com/user-attachments/assets/5a45d09a-7ae7-4994-83bf-f6568211dfca)

# 코드

```cpp
class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> v(n + 1);
        v[0] = 1;
        v[1] = 1;

        for (int i = 2; i <= n; i++){
            v[i] = v[i-1] + v[i-2];
        }

        return v[n];
    }
};
```

## 실행 결과
![image](https://github.com/user-attachments/assets/9c5864e2-f6a2-4f28-95c2-2c58772ac179)
