#include <iostream>
#include <vector>
#include <algorithm>

int l, c;
std::vector<char> s;
char arr[10] = { '\0', };
bool isused[27] = { false, };

void func(int k, int cnt1, int cnt2) {
    if (k == l) {
        // 유효한 조합인지 체크 후 출력
        if (cnt1 >= 1 && cnt2 >= 2) {
            for (int i = 0; i < l; i++) {
                std::cout << arr[i] << " ";
            }
            std::cout << "\n";
        }
        return;
    }

    for (char i : s) {
        if (k >= 1 && arr[k - 1] > i) {
            continue;  // 사전순 유지
        }

        if (!isused[i - 'a']) {
            arr[k] = i;
            isused[i - 'a'] = true;

            // 모음인지 자음인지 판단
            if (i == 'a' || i == 'e' || i == 'i' || i == 'o' || i == 'u') {
                func(k + 1, cnt1 + 1, cnt2);  // 모음 추가
            }
            else {
                func(k + 1, cnt1, cnt2 + 1);  // 자음 추가
            }

            isused[i - 'a'] = false;  // 백트래킹: 현재 문자를 다시 사용하지 않도록 설정 해제
        }
    }
}

int main(void) {
    std::cin >> l >> c;

    s.resize(c);
    for (int i = 0; i < c; i++) {
        std::cin >> s[i];
    }

    std::sort(s.begin(), s.end());  // 사전순 정렬
    func(0, 0, 0);  // 초기 호출 시 cnt1, cnt2는 0부터 시작
    return 0;
}
