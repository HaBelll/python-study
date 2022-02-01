#조건문(if문)
from operator import truediv


money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#비교 연산자로 구해보기
a = 1
b = 2
if a < b:
    print("버스를 타고 가라")
else:
    print("택시를 타고 가라")

#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 
#그렇지 않으면 걸어 가라
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#in
money = 2000
card = 1
if 1 in [1,2,3]:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#not in
money = 2000
card = 1
if 1 not in [1,2,3]:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#조건문에서 아무 일도 하지 않게 설정하기 pass 사용
money = 2000
card = 1
if 1 in [1,2,3]:
    pass
else:
    print("걸어가라")

#다중 조건 판단 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("버스를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

#조건부 표현식
score = 70
message = "success" if score >= 60 else "failure"
print(message)

#반복문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

#break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 준다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
#continue
a = 0
while a < 10:
    a = a+1
    if a % 2 == 0:
        continue
    print(a)

#for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#다양한 for문의 사용 
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#60점이 넘으면 합격 그렇지 않으면 불합격
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

#for와 함께 자주 사용하는 range함수
sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)

#구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')