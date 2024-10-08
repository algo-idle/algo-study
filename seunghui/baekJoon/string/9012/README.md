# 9012번: 괄호

## 문제
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

## 문제 설명
데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 
하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/a9d64179-195f-43da-abaf-e10e3d206686)

### Example 2:  
![image](https://github.com/user-attachments/assets/604e8772-5691-4954-ad82-ddd83e678f83)

# 코드 1
```cpp
#include <iostream>
#include <vector>
#include <string>

int main(void) {
    int t;
    std::cin >> t;
    
    while (t--){
        std::string s;
        std::cin >> s;
        
        int cnt = 0;
        for (int i = 0; i < s.length(); i++){
            if (s[i] == '('){
                cnt++;
            }
            else if (s[i] == ')'){
                cnt--;
            }
            
            if (cnt < 0){
                break;
            }
        }
        
        if (cnt == 0){
            std::cout << "YES";
        }
        else{
            std::cout << "NO";
        }
        std::cout << "\n";
    }

    return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/62492406-3d58-45f2-a4db-c80cf9c89746)


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/e53a838a-0ac9-4fcc-9932-54d0500f898a)

12시 지나고 제출해서 공백이 2칸이 생겼네..  
(8/15 광복절 -> 휴식 , 8/16 12시 지나고 제출 -> 공백..)
