#튜플은 추가하고 삭제하고 할수없고 고정 리스트랑 다르다
#t1 = (1,2,'a','b')
#del t1[0]

#딕셔너리는 Key를 통해 Value를 얻는다.
dic = {'name': 'hajonghyeon', 'age': 25}

print(dic['age'])

#딕셔너리 쌍 추가하기
a = {1: 'a'}
a['name'] = "익명"

print(a)

#딕셔너리에서 Key랑 Value 뽑기
a = {1: '하종현', 2: '이정민', 3: '이민지'}
print(a.keys())
print(a.values())
print(a.items())

#딕셔너리 모두 지우기
a = {1: '하종현', 2: '이정민', 3: '이민지'}
a.clear
print(a)

#딕셔너리 안에 key가 있는지 조사하기
a = a = {1: '하종현', 2: '이정민', 3: '이민지'}

print(4 in a)

#집합은 중복을 허용하지않는다, 순서가 없다
s1 = set([1,2,3])

print(s1)

#교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)

#합집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 | s2)

#차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 - s2)

#집합에 값 1개 추가할때
s1 = set([1, 2, 3, 4, 5, 6])
s1.add(7)
print(s1)
#집합에 값 여러개 추가할때
s1 = set([1, 2, 3, 4, 5, 6])
s1.update([7, 8, 9])
print(s1)

#불=true or false
a = True
print(type(a))

#pop으로 뒤에 하나씩지우기
a = [1,2,3,4]
while a:
    a.pop()
    print(a)

#변수 같은주소일때 
a = [1,2,3]
b = a
a[1] = 4
print(a)
print(b)
#다른주소일때
a = [1,2,3]
b = a[:]
a[1] = 4
print(a)
print(b)

#서로 값 바꾸기
a = 3
b = 5
a,b = b,a
print(a)
print(b)