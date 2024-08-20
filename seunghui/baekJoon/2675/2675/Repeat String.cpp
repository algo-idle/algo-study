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