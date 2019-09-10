# 1. for 문을 사용하여 구구단을 출력하는 gugu() 함수를 만들어 호출
# 2. while 문을 사용하여 내가 원하는 단의 구구단만 출력하는
#    gugudan(x) 함수를 만들어 호출

def gugu():
    print('구구단')
    for i in range(1, 10, +1) :
        for j in range(1, 10, +1) :
            print(i,' * ',j,' = ',i*j)


def gugudan(x):
    print(str(x), '단')
    for i in range(1, 10, +1) :
        print(x,' * ',i,' = ',int(x)*i)

if __name__ == '__main__':
    gugu()
    dan = input('단 입력 : ')
    gugudan(dan)