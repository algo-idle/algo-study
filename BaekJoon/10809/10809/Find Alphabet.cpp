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

	int ver = 0;
	for (int i = 0; i < s.size() - 1; i++) {
		for (int j = i + 1; j < s.size(); j++) {
			if (s[i] == s[j]) {
				ver++;
			}
		}
		
		if (ver >= 1) {
			remove(s.begin() + i + 1, s.end(), s[i]);
			ver = 0;
		}
	}

	for (int i = 0; i < s.size(); i++) {
		res[s[i] - 97][0] = i;
	}

	for (int i = 0; i < res.size(); i++) {
		cout << res[i][0] << " ";
	}

	return 0;
}