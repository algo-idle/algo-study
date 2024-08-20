# 9012��: ��ȣ

## ����
N���� �� A1, A2, ..., AN�� �Է����� �־�����. �� M���� ���� i, j�� �־����� ��, i��° ������ j��° ������ ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.

## ���� ����
ù° �ٿ� ���� ���� N�� �־�����. (1 �� N �� 100,000) ��° �ٿ��� A1, A2, ..., AN�� �־�����. (-1,000 �� Ai �� 1,000) ��° �ٿ��� ������ ���� M�� �־�����. (1 �� M �� 100,000) ��° �ٺ��� M���� �ٿ��� �� ������ ��Ÿ���� i�� j�� �־�����. (1 �� i �� j �� N)

�� M���� �ٿ� ���� �Է����� �־��� ������ ���� ����Ѵ�.

## ����
### Example 1:  


### Example 2:  


# �ڵ� 1
```cpp
#include <iostream>
#include <vector>

int main(void) {
	int n;
	std::cin >> n;
	
	std::vector<int> nums;
	while (n--) {
		int num;
		std::cin >> num;
		nums.push_back(num);
	}

	int m;
	std::cin >> m;
	while (m--) {
		int a, b;
		std::cin >> a >> b;

		int sum = 0;
		for (int i = a - 1; i <= b - 1; i++) {
			sum += nums[i];
		}
		std::cout << sum << "\n";
	}
	return 0;
}
```
�ð� �ʰ� ��
�׷��� �ð� ���⵵�� �м��غ�

���� 'nums'�� �Է��� ���� ���� �ð� ���⵵�� 'O(n)'
���� 'a'���� 'b'������ ���� ���ϴµ�, �� ��� 'O(b - a + 1)'
�־��� ��� ������ ��ü �迭�� �ش��� ��� 'O(n)'
������ m���� �־����� �ȴٸ�, �ð� ���⵵�� 'O(m * n)'

��, n�� m�� ����� ū ��� �ð� �ʰ��� �߻��� �� ����

���� ���
1. n = 100,000
2. m = 100,000
3. ��� m���� ������ �迭 ��ü�� ���� ���ϴ� ���

�� ���ÿ����� �ð� ���⵵�� 'O(n * m) = O(10^10)'�� ��
����, 1�� �̳��� �ذ��� �� ���� ��

���� ���� ������ �ð� �ʰ��� ����, �׷��� ������ �ذ� ����� �˾ƺ� ��� "���� ��" �̶�� �˰����� ����

# �ڵ� 2
```cpp
#include <iostream>
#include <vector>

int main(void) {
	int n;
	std::cin >> n;
	
	std::vector<int> nums;
	while (n--) {
		int num;
		std::cin >> num;
		nums.push_back(num);
	}

	int m;
	std::cin >> m;
	while (m--) {
		int a, b;
		std::cin >> a >> b;

		int sum = 0;
		for (int i = a - 1; i <= b - 1; i++) {
			sum += nums[i];
		}
		std::cout << sum << "\n";
	}
	return 0;
}
```
���� �� �˰����� �������� �ұ��ϰ� �ð� �ʰ��� ����.
�׷��� ���������� cin�� cout�� ����ȭ�� ��Ȱ��ȭ�ߴ�.
�ذ�ƴ�.

# �ڵ� 3
```cpp
#include <iostream>
#include <vector>

int main(void) {
    std::ios_base::sync_with_stdio(false); 
    std::cin.tie(NULL); 

    int n;
    std::cin >> n;

    std::vector<int> nums(n + 1, 0); 
    for (int i = 1; i <= n; i++) {
        int num;
        std::cin >> num;

        // ���� �� ���
        nums[i] = nums[i - 1] + num; 
    }

    int m;
    std::cin >> m;
    while (m--) {
        int a, b;
        std::cin >> a >> b;

        // ���� �� ���
        std::cout << nums[b] - nums[a - 1] << "\n"; 
    }

    return 0;
}
```

## ä�� ���
![image](https://github.com/user-attachments/assets/62492406-3d58-45f2-a4db-c80cf9c89746)


## ��Ʈ�� (�Ǵ� �ڽ��� ���� ������ Ǯ���ٴ� ����)
![image](https://github.com/user-attachments/assets/e53a838a-0ac9-4fcc-9932-54d0500f898a)

12�� ������ Ǯ� ������ 2����..!
