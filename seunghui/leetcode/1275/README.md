# 1275번: Find Winner on a Tic Tac Toe Game

## 문제
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

## 문제 설명
주어진 배열은 A와 B가 순서대로 Tic Tac Toe 게임에서 표시한 순서이다.  
게임 결과를 출력하라

## 예시
### Example 1:  
![image](https://github.com/algo-idle/algo-study/assets/92175769/1fe5ebed-3a34-4290-8432-4f45f1bafe3a)

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]  
Output: "A"  
Explanation: A wins, they always play first.

### Example 2:     
![image](https://github.com/algo-idle/algo-study/assets/92175769/2ebd12ef-c0c4-4d87-8b30-6317e5b47bb4)

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]  
Output: "B"  
Explanation: B wins.    

### Example 3:
![image](https://github.com/algo-idle/algo-study/assets/92175769/86108a90-740d-42d9-aedb-b2b1f56dce14)

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]  
Output: "Draw"  
Explanation: The game ends in a draw since there are no moves to make.

## 코드
```cpp
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
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/2926d92a-f389-47ef-b9b8-a2b01d54b2be)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/4206f676-fb75-4624-821f-1ecdfa620e60)

풀긴 풀었는데 다시 풀어야할 문제 1 : 코드 너무 길고, 변수 너무 많이 쓴. (=> 다시 풀기.)
