# 54번: Spiral Matrix

## 문제
Given an m x n matrix, return all elements of the matrix in spiral order.

## 문제 설명
입력받은 문자열의 마지막 단어의 길이를 구하라.

## 예시
### Example 1:  
![image](https://github.com/algo-idle/algo-study/assets/92175769/08d45da8-609d-4c01-8289-0726a80cdf02)

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]  
Output: [1,2,3,6,9,8,7,4,5] 

### Example 2:     
![image](https://github.com/algo-idle/algo-study/assets/92175769/47b48979-15d2-4d6a-9565-a3da36b70472)

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

## 코드
```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<vector<int>> matrix_b(matrix.size());
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                matrix_b[i].push_back(0);
            }
        }
        vector<int> nums;
        int con_j = matrix[0].size() - 1; //2
        int con_k = matrix.size() - 1; //2
        for (int i = 0; i < matrix.size(); i++) { // 0 1 2
            for (int j = i; j <= con_j; j++) { //0 1 2
                if (matrix_b[i][j] == 0) {
                    cout << matrix[i][j] << " ";
                    nums.push_back(matrix[i][j]); //00 01 02
                    matrix_b[i][j] = 1;
                }
            }
            cout << "\n";
            for (int k = i; k <= con_k; k++) { //0 1 2
                if (matrix_b[k][con_j] == 0) {
                    cout << matrix[k][con_j] << " ";
                    nums.push_back(matrix[k][con_j]); //02 12 22
                    matrix_b[k][con_j] = 1;
                }
            }
            for (int l = con_j; l >= i; l--) { //2 1 0
                if (matrix_b[con_k][l] == 0) {
                    nums.push_back(matrix[con_k][l]); //22 21 20
                    matrix_b[con_k][l] = 1;
                }
            }

            if (con_j > 0) {
                con_j--; //1
            }
            if (con_k > 0) {
                con_k--; //8
            }
            for (int m = con_k; m >= i; m--) { // 8 7 6 5 4 3 2 1 0
                if (con_j >= 1) {
                    if (matrix_b[m][i] == 0) {
                        nums.push_back(matrix[m][i]); // 11 01
                        matrix_b[m][i] = 1;
                    }
                }
                else {
                    if (matrix_b[m][con_j] == 0) {
                        nums.push_back(matrix[m][con_j]); // 11 01
                        matrix_b[m][con_j] = 1;
                    }
                }
            }
        }
        return nums;
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/73dab828-6817-4e17-a068-ae2739cb120f)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/aa79f527-0e9c-4d10-b9e4-397e785d4d7d)
