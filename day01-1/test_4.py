#문자열 인덱싱&슬라이싱
s = 'Hello World!'
print('len(s) : ', len(s))
print(s.count('o'))
print(s[6:])                    #해당 문자열의 6번 인덱스를 포함하여 다음 인덱스의 문자들을 전부 출력하라
print(' ! : ', s[11])
print('s[-2] : ', s[-2])        #-2 = 0-2
print('Hello : ', s[:5])        #해당 문자열의 5번 인덱스를 제외하고 이전 인덱스의 문자들을 전부 풀력하라
print('All : ', s[:])
print(s[0:8:2])                 #인덱스 0부터8까지, 2이하 수의 인덱스 항목은 제외하여 출력한다. 0의 경우는 무조건 포함되어야 하무로 제외 항목에서 제외한다.

#문자열 데이터는 문자열 자체를 변경시킬 수는 없다.
print('h' + s[1:])              #가라로 변경시켜주는 연출만 한다.
print('s : ', s)

greeting = "hellow world"
print(greeting[::-1])           #[::-1]은 문자열 전체를 역순으로 나타내준다.