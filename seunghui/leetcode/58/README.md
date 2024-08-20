# 58번: Length of Last Word

## 문제
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

## 문제 설명
입력받은 문자열의 마지막 단어의 길이를 구하라.

## 예시
### Example 1:  
Input: s = "Hello World"  
Output: 5  
Explanation: The last word is "World" with length 5.  

### Example 2:     
Input: s = "   fly me   to   the moon  "  
Output: 4  
Explanation: The last word is "moon" with length 4.  

### Example 3:   
Input: s = "luffy is still joyboy"  
Output: 6  
Explanation: The last word is "joyboy" with length 6.  

## 코드
```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        int cnt = 0;
        for (int i = s.length() - 1; i >= 0; i--){
            if (s[i] != ' '){
                std::cout << s[i];
                cnt++;
                if (i-1 >= 0){
                    if (s[i-1] == ' '){
                    break;
                    }
                }
            }
        }

        return cnt;
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/f20a47d3-a3ba-48b5-83f8-bb02e88cb4a5)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/f14a1127-a8df-4036-9177-e293dfed2e5b)
