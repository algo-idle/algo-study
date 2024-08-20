#include <iostream>
#include <vector>

using namespace std;

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

int main(void) {

    vector<vector<int>> matrix1 = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    vector<vector<int>> matrix2 = { {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12} };
    vector<vector<int>> matrix3 = { {7}, {9}, {6} };
    vector<vector<int>> matrix4 = { {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10} };

    Solution s;
    vector<int> res;
    res = s.spiralOrder(matrix1);

    for (int i = 0; i < res.size(); i++) {
        std::cout << res[i] << " ";
    }

	return 0;
}