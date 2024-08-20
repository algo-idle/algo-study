# 1572번: Matrix Diagonal Sum

## 문제Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

## 문제 설명
2차원 행렬에서 대각선 요소들을 모두 더해서 출력하라.

## 예시
### Example 1:  
Input: mat = [[1,2,3],  
              [4,5,6],  
              [7,8,9]]  
Output: 25  
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25  
Notice that element mat[1][1] = 5 is counted only once.  

### Example 2:     
Input: mat = [[1,1,1,1],  
              [1,1,1,1],  
              [1,1,1,1],  
              [1,1,1,1]]  
Output: 8  

### Example 3:
Input: mat = [[5]]  
Output: 5

## 코드
```cpp
class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int size = mat[0].size();

        int sum = 0;
        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++){
                if (i == j){
                    std::cout << mat[i][j] << " ";
                    sum += mat[i][j];
                }
            }
        }

        for (int i = 0; i < size; i++){
            for (int j = size-i-1; j >= 0; j--){
                std::cout << mat[i][j] << " ";
                sum += mat[i][j];
                break;
            }
        }

        if (size % 2 != 0){
            int index = size / 2;
            sum -= mat[index][index];
        }
        return sum;
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/84967089-d6fa-433c-8fdb-5719df94171f)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/d4c1d3c4-a4b3-42db-9446-8a84f1ff6a4f)

