# 73번: Set Matrix Zeroes

## 문제
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

## 문제 설명
주어진 행렬에서 0인 요소가 있다면, 그 요소가 포함된 행과 열을 모두 0으로 만들어라.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/40138d00-9421-4cb7-864d-6087f6ab2faa)  
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]  
Output: [[1,0,1],[0,0,0],[1,0,1]]

### Example 2:     
![image](https://github.com/user-attachments/assets/08ab99ab-3958-487f-aede-82f9d8b6bd00)  
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]  
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## 코드
```cpp
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<int> posx;
        vector<int> posy;
        for (int i = 0; i < matrix.size(); i++){
            for (int j = 0; j < matrix[0].size(); j++){
                if (matrix[i][j] == 0){
                    posx.push_back(i);
                    posy.push_back(j);
                }
            }
        }

        for (int i = 0; i < posx.size(); i++){
            for (int j = 0; j < matrix.size(); j++){
                matrix[j][posy[i]] = 0;
            }

            for (int k = 0; k < matrix[0].size(); k++){
                matrix[posx[i]][k] = 0;
            }
        }
    }
};
```

## 채점 결과
![image](https://github.com/user-attachments/assets/bf7e69ba-2bb1-47c0-9cae-7bffb837a309)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/9207dc48-2bd6-4738-9088-372443f83815)

