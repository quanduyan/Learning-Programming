#####################
#int

num1 = 0x23         #16진수 ==> 35
print(num1)

print(type(num1))

no1 = 1.0           #==> Float
print(type(no1))

import sys
print(sys.maxsize)  #==> 정수형 변수가 갖을 수 있는 최대값

a = 1.0
b = 3.5e3           #==> 3.5*(10^3)
print(b)

#####################
#long ==> 3버전부터는 정수는 전부 int형
h1 = 123456789012345678901234567890
print(type(h1))

num1 = 0o23         #==> 8진수
print(type(num1))
print(num1)

no2 = 0b0111000101  #==> 2진수
print(type(no2))
print(no2)


#####################
#숫자형 활용 연산자
# +, - , *, /, //, **, %
# +=, -=, *=, /=, ...

no1 = 10
no2 = 3
print(no1, no2)
print('+ : ', no1 + no2)
print('- : ', no1 - no2)
print('* : ', no1 * no2)
print('/ : ', no1 / no2)
print('% : ', no1 % no2)        #나머지 구해주는 연산자
print('** : ', no1 ** no2)      #거듭제곱 구해주는 연산자
print('// : ', no1 // no2)      #몫(정수)만 구해주는 연산자