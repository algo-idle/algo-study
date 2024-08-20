# 10871번: X보다 작은 수

## 문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.  

## 문제 설명
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)  
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.    

X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.  

## 예시
### Example 1:  
![image](https://github.com/user-attachments/assets/960d1e30-370e-473d-b440-431fd67b54f8)


# 코드 1
```cpp
#include <iostream>
#include <vector>

int main(void){
    int n, x;
    std::cin >> n >> x;
    
    std::vector<int> arr;
    for (int i = 0; i < n; i++){
        int num;
        std::cin >> num;
        arr.push_back(num);
    }
    
    for (int i = 0; i < arr.size(); i++){
        if (arr[i] < x){
            std::cout << arr[i] << " ";
        }
    }
    
    return 0;
}
```

## 채점 결과
![image](https://github.com/user-attachments/assets/c103f51a-c970-47b8-b56d-fb268dd9fc6e)


## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/user-attachments/assets/88bdd9f2-0420-4112-b285-fba677a3bab4)

