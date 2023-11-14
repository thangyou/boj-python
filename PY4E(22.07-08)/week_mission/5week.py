# 5주차 미션 목적 - 조건문, 반복문, 문자열, 리스트의 활용
# Q1. 베스킨라빈스31 게임
# 조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
# 조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
# 조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
#         -> 위 조건이 안맞을 경우 다시 입력
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

            print("---> 현재 숫자 :", numlist[-1])

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

bs31()



# Q3. 숫자 맞추기 게임
# 조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
# 조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
# 조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
import random

def guess_num():
    cnt = 0 # 시도횟수
    ans = 0 # 정답횟수
    my_list = [] # 내가 입력한 숫자
    num_list = [] # 컴퓨터의 숫자 리스트
    for i in range(3):
        num = random.randint(0, 100)
        if num not in num_list:
            num_list.append(num)
    print(num_list)

    while True:
        cnt += 1
        print(cnt,"차 시도")
        guess = int(input("숫자를 예측해보세요: "))

        if guess in my_list:
            print("이미 예측에 사용한 숫자입니다")
            cnt -= 1
            continue

        if guess in num_list:
            ans += 1
            if guess == min(num_list): print("숫자를 맞추셨습니다!", guess,"=> min")
            elif guess == max(num_list): print("숫자를 맞추셨습니다!", guess,"=> mid")
            else: print("숫자를 맞추셨습니다!", guess,"=> max")

        if guess not in num_list:
            print(guess,"는 없습니다")
            if cnt >= 5:
                if guess < min(num_list): print("min은",guess,"보다 큼")
                elif guess > min(num_list): print("min은",guess,"보다 작음")
                elif guess < max(num_list): print("max은",guess,"보다 큼")
                elif guess > max(num_list): print("max은",guess,"보다 작음")

        if ans == 3:
            print("게임종료")
            print(cnt,"번 시도만에 예측 성공")
            break

        my_list.append(guess)

guess_num()
