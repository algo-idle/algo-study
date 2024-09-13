2239번: 스도쿠 (골드 4)
| 시간 제한 | 메모리 제한 |
|:-----:|:------:|
|  2초   | 256MB  |

## 문제
스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 예를 들어 다음을 보자.



위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.

하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.


## 문제 설명
```text
1. 스택에 0인 칸을 역순으로 저장한다.
2. 백트래킹을 활용해 board를 채워나간다.
3. 스택에 남은 칸의 정보가 없다면 board를 출력하고 종료한다.
```

## 입력
9개의 줄에 9개의 숫자로 보드가 입력된다. 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.

## 출력
9개의 줄에 9개의 숫자로 답을 출력한다. 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다. 즉, 81자리의 수가 제일 작은 경우를 출력한다.## 제한
12095번 문제에 있는 소스로 풀 수 있는 입력만 주어진다.
C++17: 180ms
Java 15: 528ms
PyPy3: 2064ms


## 예제 입력 1 
```text
103000509
002109400
000704000
300502006
060000050
700803004
000401000
009205800
804000107
```
## 예제 출력 1 
```text
143628579
572139468
986754231
391542786
468917352
725863914
237481695
619275843
854396127
```


## 코드
```python
import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
zeros.sort(reverse=True)

def get_possible(x, y):
    possible = [i for i in range(1, 10)]
    for i in range(0, 9):
        if board[i][y] != 0:
            possible[board[i][y] - 1] = 0
        if board[x][i] != 0:
            possible[board[x][i] - 1] = 0

    start_x, start_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if board[i][j] != 0:
                possible[board[i][j] - 1] = 0

    return [p for p in possible if p != 0]

def sudoku():
    global board

    if zeros:
        x, y = zeros.pop()
    else:
        for b in board:
            print(''.join(str(_b) for _b in b))
        exit(0)

    possible = get_possible(x, y)
    for p in possible:
        board[x][y] = p
        sudoku()
        board[x][y] = 0

    zeros.append((x, y))

sudoku()

```

## 채점 결과
![img.png](img.png)

## 스트릭
![img_1.png](img_1.png)