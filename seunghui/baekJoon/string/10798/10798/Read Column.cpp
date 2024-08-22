#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void) {
	vector<string> s;
	for (int i = 0; i < 5; i++) {
		string str;
		getline(cin, str);
		s.push_back(str);
	}

	string res;
	for (int i = 0; i < s.size(); i++) {
		for (int j = 0; j < s[i].length(); j++) {
			if (s[j][i] == NULL) {
				break;
			}
			res += s[j][i];
		}
	}

	for (int i = 0; i < res.length(); i++) {
		cout << res[i];
	}

	return 0;
}