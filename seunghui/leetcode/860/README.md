# 860번: Lemonade Change

## 문제
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

## 문제 설명
손님들은 5, 10, 20 달러씩 낼 수 있고, 가격이 5달러인 레모네이드 한잔만 사간다.  
그랬을때, 잔돈을 거슬러 줄 수 있다면 true, 없다면 false를 출력하라.

## 예시
### Example 1:  
Input: bills = [5,5,5,10,20]
Output: true
Explanation: 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

### Example 2:     
Input: bills = [5,5,10,10,20]
Output: false
Explanation: 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.

## 코드
```cpp
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int cnt5 = 0;
        int cnt10 = 0;
        int cnt20 = 0;

        for (int i = 0; i < bills.size(); i++){
            bool change = false;
            if (bills[i] == 5){
                cnt5++;
            }
            else if (bills[i] == 10){
                if (cnt5 > 0){
                    cout << "before10: " << cnt5 << " " << cnt10 << " " << cnt20 << "\n";
                    cnt5--;
                    cnt10++;
                }
                else{
                    cout << "in1\n";
                    return false;
                }
                cout << "after10: " << cnt5 << " " << cnt10 << " " << cnt20 << "\n";
            }
            else if (bills[i] == 20 && cnt5 + cnt10 >= 2){
                cout << "before20: " << cnt5 << " " << cnt10 << " " << cnt20 << "\n";
                if ((cnt5 >= 1 && cnt10 >= 1) && change == false){
                    cnt5--;
                    cnt10--;
                    cnt20++;
                    change = true;
                }
                
                if (cnt5 >= 3 && change == false){
                    cnt5 -= 3;
                    cnt20++;
                    change = true;
                }

                if (change == false){
                    cout << "bef out" << cnt5 << " " << cnt10 << " " << cnt20 << "\n";
                    cout << "in2\n";
                    return false;
                }
                cout << "after20: " << cnt5 << " " << cnt10 << " " << cnt20 << "\n";
            }
            else{
                return false;
            }
        }
        cout << cnt5 << " " << cnt10 << " " << cnt20 << "\n";
        if (cnt5 + cnt10 + cnt20 >= 0){
            return true;
        }
        else{
            return false;
        }
        
    }
};
```

## 채점 결과
![image](https://github.com/algo-idle/algo-study/assets/92175769/9ea6130f-ce8b-4976-a3f6-5fe1ce8a0b3b)

## 스트릭 (또는 자신이 매일 문제를 풀었다는 증거)
![image](https://github.com/algo-idle/algo-study/assets/92175769/a3c5d743-4f06-4e8a-8c49-41ecc9ca76df)
