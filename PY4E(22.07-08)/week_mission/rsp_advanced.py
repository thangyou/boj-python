# Q2. 가위바위보 업그레이드.ver
# 조건 1: 게임을 몇 판 진행할지 입력 받기
# 조건 2: 0, 1, 2, 가위, 바위, 보 이외에 다른 입력 받으면 재입력 받기
# 조건 3: 게임 종료 후 나와 컴퓨터의 총 전적 출력하기
def rsp_advanced(x):
    try:
        if x == 0 or x == '가위':
            return '가위'
        elif x == 1 or x == '바위':
            return '바위'
        elif x == 2 or x == '보':
            return '보'
    except :
        return 'wrong char'

import random
Bgames = int(input("몇 판을 진행하시겠습니까? : "))
games = 2

n = 0
draw = 0
while n < games:
        computer = random.randint(0,2)
        me = random.randint(0,3)
        #me = input('가위(0) 바위(1) 보(2) :')
        print('com =', computer, 'me =', me)
        print(rsp_advanced(me))
        if rsp_advanced(me) == 'wrong char' :
            print('재')
            continue
        else :
            print("컴퓨터:", rsp_advanced(computer))

        computer = rsp_advanced(computer)
        me = rsp_advanced(me)

        if computer == '가위':
          if me == '바위':
            print("> 나의 승리")
          elif me == '보':
            print("> 컴퓨터 승리")
        elif computer == '바위':
          if me == '가위':
            print("> 컴퓨터 승리")
          elif me == '보':
            print("> 나의 승리")
        elif computer == '보':
          if me == '가위':
            print("> 나의 승리")
          elif me == '바위':
            print("> 컴퓨터 승리")
        else :
          draw = draw + 1

        n = n+1
