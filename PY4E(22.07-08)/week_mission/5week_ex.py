# Q1. 배스킨라빈스31 게임
def bs31():
    print("베스킨라빈스 써리원 게임")
    print("------------------")
    import random
    number = 0
    while True:
        # my turn
        my = input("My turn - 숫자를 입력하세요: ")
        my = my.split()
        if int(my[0]) != number + 1 or len(my) > 3:
            print("숫자를 제대로 입력하세요")
            continue
        # 숫자 2개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 2:
            if int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
        # 숫자 3개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 3:
            if int(my[2]) - int(my[1]) != 1 or int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue


        number = int(my[-1])
        print(f"현재 숫자 : {number}")

        # 31을 넘겼는지 검사
        if number >= 31:
            print("패배")
            break

        # computer
        computer = []
        computer_turn_num = random.randint(1,3)
        for i in range(computer_turn_num):
            number += 1
            # 컴퓨터가 31이 넘는 수를 외치면 31로 되돌리기
            if number > 31:
                number = number - 1
                continue
            computer.append(number)
            print(f"컴퓨터 : {computer[-1]}")
        print(f"현재 숫자 : {number}")
        print()
        # 31이 있는지 검사
        if 31 in computer:
            print("승리!")
            break
    print("게임 종료")

# 입력의 종류 예시
# 1. 정상입력
# 2. 같은숫자 입력
# 3. 범위를 벗어난 숫자 입력
bs31()

# Q2.
def grader(student, answers):
    name = [] # 이름을 분리하여 저장할 리스트
    answer = [] # 학생들의 답을 분리하여 저장할 리스트
    scores = [] # 채점후 점수를 저장할 리스트
    for s in student:
        s = s.split(",") # ,를 기준으로 이름과 정답지로 분리
        name.append(s[0])
        answer.append(s[1])

    score = 0
		# 점수 계산
		# 한 명씩 점수 계산, 답지와 내답이 같으면 10점 추가, 10문제라서 문제당 10점
    for a in answer:
        for i in range(len(a)):
            if int(a[i]) == answers[i]:
                score = score + 10
        scores.append(score)
        score = 0

		# 이름과 점수를 결합
    for i in range(len(name)):
        name[i] = str(scores[i])+name[i]
		# 점수 기준 내림차순 정렬
    name.sort(reverse=True)

		# 한 사람씩 출력
    for i in range(len(name)):
        print(f"학생: {name[i][2:]} 점수: {name[i][:2]}점 {i+1}등")

# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

grader(s,a)

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

# Q3. 숫자 맞추기 게임
import random

def guess_numbers():
    n = 3
    numbers= []
    while n > 0:
        number = random.randint(0,100)
        if number in numbers:
            continue
        else:
            numbers.append(number)
            n = n - 1

    numbers.sort()

    n = 1
    answer = 3
    my_numbers = []
    while answer > 0:
        print(f"{n}차 시도")
        my_number = int(input("숫자를 예측해보세요 : "))
        if my_number not in my_numbers:
            my_numbers.append(my_number)
        else:
            print("이미 예측에 사용한 숫자입니다")
            continue

        if my_number not in numbers:
            print(f"{my_number}는 없습니다")
            if n == 5:
                if my_number > numbers[0]:
                    print(f"최솟값은 {my_number}보다 작습니다")
                else:
                    print(f"최솟값은 {my_number}보다 큽니다")
            if n == 10:
                if my_number > numbers[2]:
                    print(f"최댓값은 {my_number}보다 작습니다")
                else:
                    print(f"최댓값은 {my_number}보다 큽니다")
            n = n + 1
            continue
        else:
            for i in range(len(numbers)):
                if numbers[i] == my_number and i == 0:
                    print(f"숫자를 맞추셨습니다! {my_number}는 최솟값입니다.")
                    n = n + 1
                    break
                elif numbers[i] == my_number and i == 1:
                    print(f"숫자를 맞추셨습니다! {my_number}는 중간값입니다.")
                    n = n + 1
                    break
                else:
                    print(f"숫자를 맞추셨습니다! {my_number}는 최댓값입니다.")
                    n = n + 1
                    break
        answer = answer - 1
    print("게임종료")
    print(f"{n-1}번 시도만에 예측 성공")

guess_numbers()

# Q4. 100일 후의 정보 계산
def after_100(month, date, day):
  # 달 별로 며칠까지 있는지 리스트로 만들기
  dates = [31,28,31,30,31,30,31,31,30,31,30,31]
  # 요일 리스트
  days = ["월","화","수","목","금","토","일"]
  after = 100

  # 파이썬 index는 0부터 시작하기 때문에 월 -1
  index = month-1

  while True:
      # 100일 음수가 될 때까지 날짜 차감
      after = after - dates[index]
      if after < 0:
          break
      # 12월 다음은 1월으로 돌아가기
      index = index + 1
      if index == 12:
          index = 0

  # 음수가된 after에 100일 후의 월의 일수를 더해주고
  # 현재 일 수를 더하고 오늘을 포함하기 때문에 -1
  date_after_100 = after + dates[index] + date -1
  # 만약 일수가 30일, 31일을 넘어가면 100일 후의 월의 일수를 빼주고 월 +1 추가
  if date_after_100 > dates[index]:
      date_after_100 = date_after_100 - dates[index]
      index = index + 1
  # 요일은 7로 나눈 나머지 만큼 움직이면 됨, 오늘을 포함하기 때문에 -1
  day_index = days.index(day)
  day_index2 = day_index + 100 % 7 -1
  # 일요일 다음은 월요일로 돌아감
  if day_index2 > (len(days) -1):
      day_index2 = day_index2 - (len(days) -1) -1
  day_after_100 = days[day_index2]

  print(f"{month}월 {date}일 {day}요일부터 100일 뒤는 {index+1}월 {date_after_100}일 {day_after_100}요일")

  # 다음년도로 넘어갈 수 있게 처리
after_100(12,3,'월')
