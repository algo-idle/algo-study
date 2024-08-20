#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main(void) {
	int num;
	cin >> num;

	stack<int> s;
	while (num > 0) {
		int de_num;
		de_num = num % 10;
		s.push(de_num);

		num /= 10;
	}

	vector<int> digit;
	while (!s.empty()) {
		digit.push_back(s.top());
		s.pop();
	}

	int size = digit.size();
	digit[size - 1] += 1;

	for (int i = 0; i < size; i++) {
		if (size == 1) {
			if (digit[i] == 10) {
				digit[size - 1] = 1;
				digit.push_back(0);
			}
		}
		if (digit[size - (i + 1)] == 10) {
			if (size - (i + 2) < 0) {
				digit[size - (i + 1)] = 1;
				digit.push_back(0);
			}
			else {
				digit[size - (i + 1)] = 0;
				digit[size - (i + 2)] += 1;
			}
		}
	}

	for (int i = 0; i < digit.size(); i++) {
		cout << digit[i];
	}

	return 0;
}