# 1157번: 단어 공부

## 문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.   
단, 대문자와 소문자를 구분하지 않는다.

## 문제 설명
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.  
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/b4b6f2b8-0d4c-4811-86f8-9be408f7bb40)

### Example 2:  
![image](https://github.com/user-attachments/assets/c624988a-0b04-4b0b-accb-553eacf6c98c)

### Example 3:  
![image](https://github.com/user-attachments/assets/7b98a66e-f60d-45a5-bef8-87b64cb24fd7)

### Example 4:  
![image](https://github.com/user-attachments/assets/4cdea266-65d8-4282-9d33-6d853f6d009d)


# 코드 1
```cpp
#include <iostream>
#include <vector>
#include <string>

int main(void) {
    std::string s;
    std::cin >> s;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] -= 32;   
        }
    }

    std::vector<int> freq(26, 0);
    
    for (int i = 0; i < s.length(); i++) {
        freq[s[i] - 'A']++;
    }
    
    int max_freq = 0;
    int max_index = -1;
    bool is_duplicate = false;

    for (int i = 0; i < 26; i++) {
        if (freq[i] > max_freq) {
            max_freq = freq[i];
            max_index = i;
            is_duplicate = false;
        } 
        else if (freq[i] == max_freq) {
            is_duplicate = true;
        }
    }

    if (is_duplicate) {
        std::cout << "?";
    } 
    else {
        std::cout << char('A' + max_index);
    }

    return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/ae5f17d6-b1c9-4991-a984-a14b2bbbba16)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/9ccaeb5c-ccf2-4431-86ba-c0af6ed41a71)
