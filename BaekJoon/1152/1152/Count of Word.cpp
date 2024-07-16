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