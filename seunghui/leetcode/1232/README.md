# 1232번: Check If It Is a Straight Line

## 문제
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

## 문제 설명
기울기가 같은 직선의 방정식에 포함되어 있는 좌표면 true, 아니면 false를 출력하라.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/be8b1e70-9074-482c-83f7-f41ce7347b6f)  
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]  
Output: true

### Example 2:     
![image](https://github.com/user-attachments/assets/1d9828b0-2399-4c26-8fda-20285c9a7e0b)  
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]  
Output: false

# 코드 1
```cpp
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        vector<int> incline;

        int isX = 0;
        int isY = 0;
        for (int i = 0; i < coordinates.size()-1; i++){
            int diff_x = coordinates[i+1][0] - coordinates[i][0];
            int diff_y = coordinates[i+1][1] - coordinates[i][1];
            // 두 좌표를 이용하여 기울기 계산
            if (diff_x != 0 && diff_y != 0){
                incline.push_back(diff_y / diff_x);
            }
            // 다음은 각각 x좌표의 차가 0, y좌표의 차가 0인 경우를 셈
            else if (diff_x == 0){
                isY++;
            }
            else if (diff_y == 0){
                isX++;
            }
        }

        // 마지막 두개의 좌표를 이용하여 기울기 계산
        int fin_x = coordinates[coordinates.size()-1][0] - coordinates[coordinates.size()-2][0];
        int fin_y = coordinates[coordinates.size()-1][1] - coordinates[coordinates.size()-2][1];
        int fin_incline = 0;
        if (fin_x != 0){
            fin_incline = fin_y / fin_x;
        }

        // 경우를 구한 것을 이용하여 true, false 반환
        if (isX == coordinates.size()-1 || isY == coordinates.size()-1){
            return true;
        }
        else if (isX >= 1 || isY >= 1){
            return false;
        }

        // 최종적으로 기울기가 모두 맞는지 구함
        for (int i = 0; i < incline.size()-1; i++){
            cout << incline[i] << " ";
            if (incline[i] != fin_incline && incline[i] != incline[i+1]){
                return false;
            }
        }

        return true;
    }
};
```

# 코드 2
```cpp
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        float diff_y = coordinates[1][1] - coordinates[0][1];
        float diff_x = coordinates[1][0] - coordinates[0][0];
        float init_incline;

        cout << diff_y << " " << diff_x << "\n";
        if (diff_y == 0){
            cout << "inY\n";
            init_incline = 0;
        }
        else if (diff_x == 0){
            cout << "inX\n";
            init_incline = coordinates[0][0];
        }
        else{
            cout << "inB\n";
            init_incline = diff_y / diff_x;
        }

        cout << init_incline << "\n";
        for (int i = 1; i < coordinates.size()-1; i++){
            float diff2_x = coordinates[i+1][0] - coordinates[i][0];
            float diff2_y = coordinates[i+1][1] - coordinates[i][1];
            float incline;

            if (diff2_y == 0){
                incline = 0;
            }
            else if (diff2_x == 0){
                incline = coordinates[i][0];
            }
            else{
                incline = diff2_y / diff2_x;
            }

            cout << incline << " ";
            if (init_incline != incline){
                return false;
            }
        }
        return true;
    }
};
```


## 채점 결과
![image](https://github.com/user-attachments/assets/c667d8c2-8470-49b1-958e-bf56843db897)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/945019d9-4a8a-4e8f-bc00-ef463dc06422)

문제 설명을 쓰면서 다시 푼게 2차 코드인데.. 1차는 어거지로 풀었다면 2차는 제대로 내가 어떻게 풀어야겠다를 알고 쓴 코드인데 왜째서 1차 코드보다 실행시간이 오래 걸렸던 것인지..
