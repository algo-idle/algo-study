# 7785번: 회사에 있는 사람

## 문제

상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

## 문제 설명

첫째 줄에 로그에 기록된 출입 기록의 수 n이 주어진다. (2 ≤ n ≤ 106) 다음 n개의 줄에는 출입 기록이 순서대로 주어지며, 각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.

회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.

현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.

## 예시

### Example 1:

![스크린샷 2024-09-26 044313](https://github.com/user-attachments/assets/bdaec2af-921a-4955-8796-6b3d4dd5d76e)


# 코드

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>

int main(void) {
	int n;
	std::cin >> n;

	std::unordered_map<std::string, std::string> um;
	while (n--) {
		std::string name;
		std::string log;
		std::cin >> name >> log;
		
		um[name] = log;
	}

	std::vector<std::string> names;
	for (auto iter : um) {
		auto _name = iter.first;
		auto _log = iter.second;
		
		if (_log == "enter") {
			names.push_back(_name);
		}
	}

	std::sort(names.begin(), names.end(), std::greater<>());

	for (int i = 0; i < names.size(); i++) {
		std::cout << names[i] << "\n";
	}
	
	return 0;
}
```

## 채점 결과

![스크린샷 2024-09-26 044147](https://github.com/user-attachments/assets/f3e75f03-0ea1-408d-9ad2-b5793b84df78)


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)

![스크린샷 2024-09-26 044220](https://github.com/user-attachments/assets/885e5a8f-99e5-4408-9586-e1adbb8986c4)
