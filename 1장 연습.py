print("Hellow World!")
# 주석

#사칙연산
a = 3
b = 4

print(a+b)
print(a*b)
print(a/b)
#몫
print(a//b)
#나머지
print(a%b)
#제곱
print(a**b)

#문자열
a = "Python's is good"

print(a)
#문자열 줄바꿈
b = 'Life is too short\nYou need python'

print(b)

#문자열 더하기
a = "Python"
b = " is fhun!"
print(a+b)

#인덱싱 긴 문자열에 각 문자마다 번호를 매긴것
a = 'Life is too short, You need python'
#플러숫자는 앞에 번호부터 마이너스는 뒤에서 부터
print(a[0])

#슬라이싱 [이상:미만:간격]
a = "20220122"
print(a[:3])

#문자열 포매팅
number = 5
day = "nine"
a = "I ate %d pizza. so I was sick for %s days." % (number, day)

print(a)

#문자열 개수 세기
a = "soccer"

print(a.count('o'))

#문자열 찾기
a = "hobby"

print(a.find('b'))

#문자열 삽입
a = ",".join('abcd')

print(a)

#대문자로 바꾸기
a = "hi"

print(a.upper())

#소문자로 바꾸기

a = "HI"

print(a.lower())


#문자 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기
a = "Life is too short"
print(a.split())

#리스트 자료형
a = ["하종현","신한세","이정민","이민지","임세현"]

print(a[1])

#리스트에 요소 추가
a = ["하종현", "이정민", "이민지"]
a.append("신한세")

print(a)

#리스트 정렬
a = [1, 4, 3]
a.sort()

print(a)

#리스트 요소 꺼내기
a = [1, 5, 3]
print(a.pop())

print(a)

#자료형 추가
a = [1, 5, 4, 2]
a.extend([9,5])
print(a)


