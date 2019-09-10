# 산술연산

a = 19
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)   # 소수점 버리기
print(a % b)    # 나머지
mok , namerge = divmod(19,4)    
print(mok)
print(namerge)
print(divmod(19,4))  

print(5**3)     #거듭제곱

#비교연산
a,b = 5,3
print(a==b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a is b)
print(a is not b)
print(True and False)
print(True or False)
print(not True)

#범위연산
list01 = list(range(100))   # 0 ~ 99
print(list01)
print(list01[2])
print(list01[12:48])        # [시작 인덱스 : 끝인덱스] -> 시작인덱스 ~ 끝 인덱스-1
print(list01[12:48:2])      # [시작 인덱스 : 끝 인덱스 : 스텝] -> 시작인덱스 ~ 끝 인덱스 -1 (스텝만큼 뛰어서)

str01 = 'Hello World! Hello Python!'
print(str01)
print(str01[6:12])
print(str01[13:])

#거꾸로
print(str01[-1])
print(str01[-2:])
print(str01[:-1])
print(str01[::-1])

# 멤버연산
list02 = [0 , 1 , 2 , 3 , 4]
print(3 in list02)
print(3 not in list02)
print(10 in list02)





