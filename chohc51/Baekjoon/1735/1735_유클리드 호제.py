from sys import *

nume1,demo1 = map(int,stdin.readline().split())
nume2,demo2 = map(int,stdin.readline().split())

demo_result = demo1*demo2
nume_result = nume1*demo2 + demo1*nume2


def gcd(a,b): #유클리드 호제법
    while b != 0:
        a,b = b,a%b
    return a
    

while gcd(demo_result,nume_result) != 1:
     i = gcd(demo_result,nume_result)
     demo_result //= i
     nume_result //= i
    
            
print(nume_result,demo_result)

