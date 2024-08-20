# 11720번: 단어의 개수

## 문제
영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

## 문제 설명
첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.  
첫째 줄에 단어의 개수를 출력한다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/c809728a-fa95-47ce-b38f-064553bc2f3b)

### Example 2:     
![image](https://github.com/user-attachments/assets/7e57f236-f4d3-4558-8c7c-e8231ba99f1a)

### Example 3:     
![image](https://github.com/user-attachments/assets/41c0860e-bf8a-4353-93f6-0111bbf100ec)

# 코드 1
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
	string s;
	getline(cin, s);

	string str;
	vector<string> cnt;
	for (int i = 0; i < s.size(); i++) {
		if (s[i] == ' ' && str != "") {
			cnt.push_back(str);
			str = "";
		}
		else if (s[i] != ' ') {
			str += s[i];
		}
	}

	if (str != "") {
		cnt.push_back(str);
	}
	cout << cnt.size();
	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/0974f413-1176-4199-938e-7b446c48f256)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/cc493cf6-e56d-4002-852d-dbe0604815ad)

7월 18일거까지 하고 7월 17일거 설명쓰느라 스트릭 연속으로 찍힌 점 참고 바람!
