# 2675번: 문자열 반복

## 문제
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

## 문제 설명
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.   
각 테스트 케이스에 대해 P를 출력한다.  

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/c280389e-4873-4ca3-9cf1-233b00238c4e)

# 코드 1
```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int t;
	cin >> t;

	while (t--) {
		int num;
		string s;

		cin >> num;
		getline(cin, s);

		for (int i = 0; i < s.size(); i++) {
			for (int j = 0; j < num; j++) {
				if (s[i] != ' ') {
					cout << s[i];
				}
			}
		}

		cout << "\n";
	}

	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/eabc8fe3-2775-4958-afbc-4a372aa82512)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/413abd5e-5063-464e-912a-688113e2cef9)