# 1620번: 나는야 포켓몬 마스터 이다솜

## 문제

그럼 다솜아 이제 진정한 포켓몬 마스터가 되기 위해 도감을 완성시키도록 하여라. 일단 네가 현재 가지고 있는 포켓몬 도감에서 포켓몬의 이름을 보면 포켓몬의 번호를 말하거나, 포켓몬의 번호를 보면 포켓몬의 이름을 말하는 연습을 하도록 하여라. 나의 시험을 통과하면, 내가 새로 만든 도감을 주도록 하겠네.

## 문제 설명

첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~

## 예시

### Example 1:

![스크린샷 2024-09-26 044654](https://github.com/user-attachments/assets/90f19db7-3e08-4bdb-a4ad-1607af7919dd)

# 코드

```cpp
#include <iostream>
#include <unordered_map>
#include <string>

int main(void) {
	//입출력 속도 최적화를 위해 사용
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);

	//도감에 수록되어 있는 포켓몬의 개수 n
	//내가 맞춰야 하는 문제의 개수 m
	int n, m;
	std::cin >> n >> m;

	std::unordered_map<int, std::string> num_to_name;
	std::unordered_map<std::string, int> name_to_num;

	int num = 1;
	while (n--) {
		std::string name;
		std::cin >> name;

		num_to_name[num] = name;
		name_to_num[name] = num;
		num++;
	}

	while (m--) {
		std::string answer;
		std::cin >> answer;

		//숫자라면
		if (isdigit(answer[0])) {
			int num_answer = std::stoi(answer);
			std::cout << num_to_name[num_answer] << "\n";
		}
		//문자열이라면
		else {
			std::cout << name_to_num[answer] << "\n";
		}
	}
	return 0;
}
```

## 채점 결과

![스크린샷 2024-09-26 044722](https://github.com/user-attachments/assets/c2d90c9d-517a-466d-826c-5ee188f57316)


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)

![스크린샷 2024-09-26 044735](https://github.com/user-attachments/assets/b896de0b-9203-432e-aa79-17887cfd6d55)
