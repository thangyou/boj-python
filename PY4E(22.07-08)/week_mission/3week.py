# Q1. 구구단 출력
# 조건 1: 홀수번째만 출력
# 조건 2: 값이 50이하인 것만 출력
def gugudan(num):
    print(num,"단")
    for i in range(1,10,2):
        if num * i <= 50:
            print(num,'X',i,'=',num*i)

num = int(input('몇 단? : '))
gugudan(num)

# Q2. 가위바위보 업그레이드.ver
# 조건 1: 게임을 몇 판 진행할지 입력 받기
# 조건 2: 0, 1, 2, 가위, 바위, 보 이외에 다른 입력 받으면 재입력 받기
# 조건 3: 게임 종료 후 나와 컴퓨터의 총 전적 출력하기

# Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수
# 중앙값도 함께 출력하되 중앙값이 짝수가 아닐 경우에는 출력하지 않음
def find_even_num(n, m):
    mid = int((n+m)/2)
    print('mid : ', mid)
    numbers = [i for i in range(n, m+1)]
    for i in numbers:
        if i % 2 == 0:
            print(i, '짝수')
            if i == mid:
                print(i, '중앙값')


n = int(input('첫 번째 수 입력 : '))
m = int(input('두 번째 수 입력 : '))
find_even_num(n,m)

# Q4. 2개의 숫자를 입력하여 소수가 몇 개인지 출력하는 함수
