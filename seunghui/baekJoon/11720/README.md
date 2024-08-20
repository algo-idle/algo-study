# 11720번: 숫자의 합

## 문제
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

## 문제 설명
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.  
입력으로 주어진 숫자 N개의 합을 출력한다.

## 예시
### Example 1:  
![스크린샷 2024-07-18 232150](https://github.com/user-attachments/assets/832d320e-2377-48bc-bc87-3a761dee306c)

### Example 2:     
![image](https://github.com/user-attachments/assets/0d60fd06-a539-4a6a-9103-c028b45879b5)

### Example 3:     
![image](https://github.com/user-attachments/assets/6b8c342f-e284-4af6-876f-767dcf726044)

### Example 4:     
![image](https://github.com/user-attachments/assets/f10c149c-9cfa-4d7f-b312-576591f4b32c)

# 코드 1
```cpp
#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	string s;
	cin >> s;

	int sum = 0;
	for (int i = 0; i < s.size(); i++) {
		sum += s[i] - '0';
	}

	cout << sum;
	return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/d2e35dac-1a8a-4db1-84d1-e330635367bd)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/cc493cf6-e56d-4002-852d-dbe0604815ad)

7월 18일거까지 하고 7월 17일거 설명쓰느라 스트릭 연속으로 찍힌 점 참고 바람!
