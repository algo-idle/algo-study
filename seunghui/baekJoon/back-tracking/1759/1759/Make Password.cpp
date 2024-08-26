#include <iostream>
#include <vector>
#include <algorithm>

int l, c;
std::vector<char> s;
char arr[10] = { '\0', };
bool isused[27] = { false, };

void func(int k, int cnt1, int cnt2) {
    if (k == l) {
        // ��ȿ�� �������� üũ �� ���
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
            continue;  // ������ ����
        }

        if (!isused[i - 'a']) {
            arr[k] = i;
            isused[i - 'a'] = true;

            // �������� �������� �Ǵ�
            if (i == 'a' || i == 'e' || i == 'i' || i == 'o' || i == 'u') {
                func(k + 1, cnt1 + 1, cnt2);  // ���� �߰�
            }
            else {
                func(k + 1, cnt1, cnt2 + 1);  // ���� �߰�
            }

            isused[i - 'a'] = false;  // ��Ʈ��ŷ: ���� ���ڸ� �ٽ� ������� �ʵ��� ���� ����
        }
    }
}

int main(void) {
    std::cin >> l >> c;

    s.resize(c);
    for (int i = 0; i < c; i++) {
        std::cin >> s[i];
    }

    std::sort(s.begin(), s.end());  // ������ ����
    func(0, 0, 0);  // �ʱ� ȣ�� �� cnt1, cnt2�� 0���� ����
    return 0;
}
