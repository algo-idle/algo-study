#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
	bool repeatedSubstringPattern(string s) {
		int length = s.length();

		//약수 찾기
		std::vector<int> yak;
		for (int i = 2; i <= length; i++)
		{
			if (length % i == 0) {
				yak.push_back(i);
			}
		}

		// 각 약수 길이의 sub_str을 yak_s에 삽입
		std::vector<std::string> yak_s;
		for (int i = 0; i < yak.size(); i++) {
			std::string tmp;
			for (int j = 0; j < yak[i]; j++) {
				tmp += s[j];
			}
			yak_s.push_back(tmp);
		}

		// 각 약수의 길이만큼의 sub_str이 원래 문자열에 들어있는 개수 구하기
		std::vector<int> split;
		for (int i = 0; i < yak.size(); i++) {
			split.push_back(length / yak[i]);
		}

		// sub_str을 구해서 같을 경우 cnt 증가
		// cnt 통해서 true/false 결과값 구하기
		std::vector<std::string> split_strs;
		for (int i = 0; i < split.size(); i++) {
			//std::cout << split[i] << " ";

			int cnt = 0;
			for (int k = 0; k < s.length() / split[i]; k++) {

				if (k + 1 <= s.length() / split[i]) {
					std::string split_str;
					for (int j = k * split[i]; j < (k + 1) * split[i]; j++) {
						split_str += s[j];
					}

					if (k > 0) {
						if (split_strs[i] == split_str) {
							//std::cout << split_strs[0] << " " << split_str << "\n";
							split_strs.push_back(split_str);
							cnt++;
						}
					}
					else {
						split_strs.push_back(split_str);
					}
				}
			}
			if (cnt == length / split[i] - 1) {
				return true;
			}
		}
		return false;
	}
};

int main(void) {
	std::string s;
	std::cin >> s;

	Solution sol;
	std::cout << sol.repeatedSubstringPattern(s);
}