no1, no2 = 10, 11
print('no1 no2 print: ', no1, no2)
#print('no1 no2 print: '+ no1 + no2) 이런 경우에는 데이터 타입이 달라 연산이 불가능하다.
print('2. no1 no2 print : ' + str(no1) + ' ' + str(no2))

e=5.6

f=3.5

e, f = f, e

print(e,f)


list1 = range(1,10)
print(list1)

a=2
b=4+a
a += b
print(a)
a **= 2
print(a)
a //= 2     # //는 정수형으로 값을 반환하고, /는 실수형으로 값을 반환한다.
print(a)
a -= 3+3    # 3+3먼저 연산한 뒤 a에서 빼주고 대입한다.
print(a)

str1 = str(100)

num = '123'
print(int(num)-100)

#k=int(input('int: '))
#print(k)
#print(type(k))

print(4+5, 4-2)
print(1)
print(2)

