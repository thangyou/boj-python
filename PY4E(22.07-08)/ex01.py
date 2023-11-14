'''
Q1. 베스킨라빈스31 게임
조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
        -> 위 조건이 안맞을 경우 다시 입력
추가 예정
조건4 - 중복값 입력 시, 재입력받기
조건5 -
'''
import random

def bs31():
    print("베스킨라빈스 떠리원 헤이\n")

    # my 와 com 의 번호 저장
    numlist = list()

    try:
        while True:
            # my_turn
            my_turn = input('My turn - ')
            if my_turn == "":
                break
            my_turn = my_turn.split()
            # my_turn = map(int, input('My turn : ').split())

            if len(my_turn) == 1:
                if len(numlist) == 0: # 첫 실행 시, 그냥 저장만 해.
                    numlist.append(my_turn[0])
                # my_turn[-2]가 존재하지 않으므로 numlist[-1]과 비교
                elif int(my_turn[-1]) != int(numlist[-1]) + 1:
                    print("--- 재입력 ---")
                    continue
                else:
                    numlist.append(my_turn[0])

            elif len(my_turn) == 2:
                # 조건 3) 만족
                if int(my_turn[-1]) == int(my_turn[0]) + 1:
                    for i in range(len(my_turn)):
                        numlist.append(my_turn[i])

            elif len(my_turn) == 3:
                # 조건3) 만족
                if int(my_turn[-1]) == int(my_turn[-2]) + 1 and int(my_turn[-1]) == int(my_turn[0]) + 2:
                    for i in range(len(my_turn)):
                        numlist.append(my_turn[i])

            #조건 2) 불만족
            else:
                print("--- 재입력 ---")
                continue

            # 출력 formatting
            # print("---> 현재 숫자 :", numlist[-1])
            # print("---> 현재 숫자 : {numlist}" .format(numlist=numlist[-1]))
            print(f"---> 현재 숫자 : {numlist[-1]}")

            # 종료 조건 확인
            if '31' in numlist:
                print('YOU LOSE')
                break

            #com_turn
            for i in range(random.randint(1,3)):
                com_turn = int(numlist[-1]) + 1
                numlist.append(com_turn)
                print('Computer turn -',com_turn)
                if com_turn == 30 or com_turn == 31: break

            print("---> 현재 숫자 :", numlist[-1])

            # 종료 조건 확인
            if int(numlist[-1]) == 31:
                print('COMPUTER LOSE')
                break

    except Exception as e:
        print(e)

# ------------------
bs31()
