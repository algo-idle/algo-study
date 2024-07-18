# 11720번: 단어의 개수

## 문제
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

## 문제 설명
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.  
  
각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/6436ff9d-342d-4257-921e-7efdb3b7cb5e)

# 코드 1
```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
	string s;
	cin >> s;

	vector<vector<int>> res (26);
	for (int i = 0; i < res.size(); i++) {
		res[i].push_back(-1);
	}

	for (int i = s.size() - 1; i >= 0; i--) {
		//cout << i << " " << s[i] << "\n";
		res[s[i] - 97][0] = i;
	}

	for (int i = 0; i < res.size(); i++) {
		cout << res[i][0] << " ";
	}

	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/c9234275-bcf7-49ba-8594-6e9b8156fa92)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/cc493cf6-e56d-4002-852d-dbe0604815ad)
