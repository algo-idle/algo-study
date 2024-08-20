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