#문자열 형식
"""
    '', ""로 표현한다.
    ''' ''' ==> 여러줄 문자열을 표현할 경우 사용
    ''와 ""의 구분은 없다.
"""

str1 = 'Hello World!'
str2 = "Hello World!"
print('str1 : ', str1)
print('str2 : ', str2)

str3 = '\'Hello\' World!'       #역슬래쉬(\)를 써주면 따옴표를 중복하여 사용해도 에러가 나지 않는다.
str4 = "'Hello' World!"         #그러나 이렇게 하면 어떨까
print('str3 : ', str3)
print('str4 : ', str4)

str5 = """Oasis
Blur
"""                             #큰따옴표 3개(""" """)로 멀티 라인 표현가능
print(str5)

str6 = 'Oasis\
\nBlur\
'
print(str6)                     #\n은 줄바꿈 기호