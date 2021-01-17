print("Hello World")

print("\n=============1==============")
print(1 == 1)       # True
print(not(1 == 1))  # False
print(2 or True)   # 2
print(True or 2)   # True
print(3 and True)   # True

print("\n=============2==============")
print(14 // 3)  # 4 (몫
print(14 % 3)   # 2 (나머지
print(5 ** 3)   # 125

print("\n=============3==============")
from random import *
print( int(random() * 10 + 1) )    # 0 <= random < 1   # 1 <= random * 10 + 1 < 11
print( randint(1, 5) )      # 1 <= randint <= 5
print( randrange(1, 5) )    # 1 <= randrange < 5


print("\n=============4==============")
print( abs(-11) )   # 절댓값
print( pow(5, 3) )  # 5^3   == 5**3
print( round(5.155) )   # 반올림
num = 5.575
print( round(num) )   # 반올림
print( round(num*10)/10 )   # 소수점 아래 2번째에서 반올림
print( type(num) )


print("\n=============5==============")
from math import *
print( floor(5.98) )   # 내림
print( ceil(5.11) )   # 올림
print( sqrt(9) )   # 제곱근
