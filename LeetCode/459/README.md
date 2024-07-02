# 459번: Repeated Substring Pattern

## 문제
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

## 문제 설명
문자열 s에 서브 문자열이 여러개 포함되어 있다면 true, 아니면 false를 출력하라.

## 예시
### Example 1:
Input: s = "abab"   
Output: true   
Explanation: It is the substring "ab" twice.   

### Example 2:   
Input: s = "aba"   
Output: false   

### Example 3:   
Input: s = "abcabcabcabc"   
Output: true   
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.   

## 코드
```cpp
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int length = s.length();

        //약수 찾기
        std::vector<int> yak;
        for (int i = 2; i <= length; i++)
        {
            if (length % i == 0) {
                yak.push_back(i);
            }
        }

        std::vector<std::string> yak_s;
        for (int i = 0; i < yak.size(); i++) {
            std::string tmp;
            for (int j = 0; j < yak[i]; j++) {
                tmp += s[j];
            }
            yak_s.push_back(tmp);
        }

        std::vector<int> split;
        for (int i = 0; i < yak.size(); i++) {
            split.push_back(length / yak[i]);
        }

        std::vector<std::string> split_strs;
        for (int i = 0; i < split.size(); i++) {
            std::cout << split[i] << " ";
            
            int cnt = 0;
            for (int k = 0; k < s.length() / split[i]; k++) {
                
                if (k + 1 <= s.length() / split[i]) {
                    std::string split_str;
                    for (int j = k * split[i]; j < (k + 1) * split[i]; j++) {
                        split_str += s[j];
                    }
                    
                    if (k > 0) {
                        if (split_strs[i] == split_str) {
                            std::cout << split_strs[0] << " " << split_str << "\n";
                            split_strs.push_back(split_str);
                            cnt++;
                        }
                    }
                    else {
                        split_strs.push_back(split_str);
                    }
                }
            }
            if (cnt == length / split[i] - 1) {
                return true;
            }
        }
        return false;
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/33742786-eed3-4aaf-a632-0f37ded76356)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/1b42a7a3-9edf-4b78-8904-71a700364fb7)