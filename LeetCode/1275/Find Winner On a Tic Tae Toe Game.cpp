#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<char>> matrix(3);
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                matrix[i].push_back('N');
            }
        }

        for (int i = 0; i < moves.size(); i++) {
            if (i % 2 == 0) {
                matrix[moves[i][0]][moves[i][1]] = 'A';
            }
            else {
                matrix[moves[i][0]][moves[i][1]] = 'B';
            }
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << "\n";
        }

        int cnt_raw_a = 0;
        int cnt_raw_b = 0;
        int cnt_col_a = 0;
        int cnt_col_b = 0;
        int cnt_dia_a1 = 0;
        int cnt_dia_b1 = 0;
        int cnt_dia_a2 = 0;
        int cnt_dia_b2 = 0;

        int n = 0;
        int cnt_a = 0;
        int cnt_b = 0;

        for (int i = 0; i < 3; i++) {
            if (cnt_raw_a < 3) {
                cnt_raw_a = 0;
            }
            if (cnt_raw_b < 3) {
                cnt_raw_b = 0;
            }
            if (cnt_col_a < 3) {
                cnt_col_a = 0;
            }
            if (cnt_col_b < 3) {
                cnt_col_b = 0;
            }

            for (int j = 0; j < 3; j++) {
                if (matrix[i][j] == 'A') {
                    cnt_raw_a++;
                    if (cnt_raw_a == 3) {
                        cnt_a++;
                    }
                }
                if (matrix[i][j] == 'B') {
                    cnt_raw_b++;
                    if (cnt_raw_b == 3) {
                        cnt_b++;
                    }
                }

                if (matrix[j][i] == 'A') {
                    cnt_col_a++;
                    if (cnt_col_a == 3) {
                        cnt_a++;
                    }
                }
                if (matrix[j][i] == 'B') {
                    cnt_col_b++;
                    if (cnt_col_b == 3) {
                        cnt_b++;
                    }
                }

                if (matrix[i][j] == 'N') {
                    n++;
                }

                if (i == j) {
                    if (matrix[i][j] == 'A') {
                        cnt_dia_a1++;
                    }
                    else if (matrix[i][j] == 'B') {
                        cnt_dia_b1++;
                    }

                    if (matrix[i][2-j] == 'A') {
                        cnt_dia_a2++;
                    }
                    else if (matrix[i][2-j] == 'B') {
                        cnt_dia_b2++;
                    }
                }
            }
        }

        cout << "cnt_raw_a " << cnt_raw_a << "\n";
        cout << "cnt_raw_b " << cnt_raw_b << "\n";
        cout << "cnt_col_a " << cnt_col_a << "\n";
        cout << "cnt_col_b " << cnt_col_b << "\n";
        cout << "cnt_dia_a1 " << cnt_dia_a1 << "\n";
        cout << "cnt_dia_b1 " << cnt_dia_b1 << "\n";
        cout << "cnt_dia_a2 " << cnt_dia_a2 << "\n";
        cout << "cnt_dia_b2 " << cnt_dia_b2 << "\n";

        if (cnt_raw_a == 3 || cnt_col_a == 3 || cnt_dia_a1 == 3 || cnt_dia_a2 == 3) {
            cnt_a++;
        }
        else if (cnt_raw_b == 3 || cnt_col_b == 3 || cnt_dia_b1 == 3 || cnt_dia_b2 == 3) {
            cnt_b++;
        }

        cout << "cnt_a " << cnt_a << "\n";
        cout << "cnt_b " << cnt_b << "\n";

        if (cnt_a > cnt_b) {
            return "A";
        }
        else if (cnt_b > cnt_a) {
            return "B";
        }
        else if (cnt_a == cnt_b && n == 0){
            return "Draw";
        }
        return "Pending";
    }
};

int main(void) {
    vector <vector<int>> a1;
    vector <vector<int>> a2;
    vector <vector<int>> a3;
    vector <vector<int>> a4;
    vector <vector<int>> a5;

    a1 = { {0, 0} ,{2, 0},{1, 1},{2, 1},{2, 2} };
    a2 = { {0, 0} ,{1, 1},{0, 1},{0, 2},{1, 0},{2, 0} };
    a3 = { {0, 0} ,{1, 1},{2, 0},{1, 0},{1, 2},{2, 1},{0, 1},{0, 2},{2, 2} };
    a4 = { {0, 0} ,{1, 1} };
    a5 = { {2, 2} ,{0, 2},{1, 0},{0, 1},{2, 0},{0, 0} };

    Solution s;
    cout << s.tictactoe(a5);
	return 0;
}