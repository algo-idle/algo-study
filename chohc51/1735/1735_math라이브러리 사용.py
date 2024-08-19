from sys import *
import math

nume1,demo1 = map(int,stdin.readline().split())
nume2,demo2 = map(int,stdin.readline().split())

demo_result = demo1*demo2
nume_result = nume1*demo2 + demo1*nume2


while math.gcd(demo_result,nume_result) != 1:
    i = math.gcd(demo_result,nume_result)
    demo_result //= i
    nume_result //= i
    
            
print(nume_result,demo_result)

