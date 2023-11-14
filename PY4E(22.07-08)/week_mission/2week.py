# Q1. 컴퓨터와 함께하는 가위바위보 게임
# 조건 1: 함수의 인자로는 나의 가위바위보 선택이 들어감 (0,1,2 혹은 가위,바위,보로 입력 = 총 6가지)
# 조건 2: 누가 무엇을 냈고, 누가 승리했는지 출력이 되어야 함

import random

def rsp(my):
    if my == '0' or my == '가위':
        print('나: 가위')
        if com == 0:
            print('컴퓨터: 가위')
            print('무승부!')
        elif com == 1:
            print('컴퓨터: 바위')
            print('컴퓨터 승리!')
        else:
            print('컴퓨터: 보')
            print('나 승리!')
    elif my == '1' or my == '바위':
        print('나: 바위')
        if com == 0:
            print('컴퓨터: 가위')
            print('나 승리!')
        elif com == 1:
            print('컴퓨터: 바위')
            print('무승부!')
        else:
            print('컴퓨터: 보')
            print('컴퓨터 승리!')
    else:
        print('나: 보')
        if com == 0:
            print('컴퓨터: 가위')
            print('컴퓨터 승리!')
        elif com == 1:
            print('컴퓨터: 바위')
            print('나 승리!')
        else:
            print('컴퓨터: 보')
            print('무승부!')

com = random.randint(0,2)
my = input("가위(0) 바위(1) 보(2) ~ ")
rsp(my)

# Q2. 월급을 입력하면 연봉을 계산해주는 계산기
def yearly_pay(m_p):
    y_p = m_p * 12
    print('세전 연봉 : ', y_p,"만원")
    if y_p <= 1200:
        tax = y_p * 0.06
    elif y_p <= 4600 and y_p > 1200:
        tax = y_p * 0.15
    elif y_p <= 8800 and y_p > 4600:
        tax = y_p * 0.24
    elif y_p <= 15000 and y_p > 8800:
        tax = y_p * 0.35
    elif y_p <= 30000 and y_p > 15000:
        tax = y_p * 0.38
    elif y_p <= 50000 and y_p > 30000:
        tax = y_p * 0.40
    else:
        tax = y_p * 0.42

    print('세후 연봉 : ', int(y_p - tax),'만원')

monthly_pay = 300
yearly_pay(monthly_pay)

# Q3. 학생 이름과 점수를 입력하면 학점 출력하는 학점 변환기
def grader(name, score):
    print('학생 이름 : ', name)
    print('점수 : ', score)
    if score >= 95 and score < 101:
        grade = 'A+'
    elif score >= 90 and score < 95:
        grade = 'A'
    elif score >= 85 and score < 90:
        grade = 'B+'
    elif score >= 80 and score < 85:
        grade = 'B'
    elif score >= 75  and score < 80:
        grade = 'C+'
    elif score >= 70 and score < 75:
        grade = 'C'
    elif score >= 65 and score < 70:
        grade = 'D+'
    elif score > 60 and score < 65:
        grade = 'D'
    else:
        grade = 'F'

    print('학점 : ', grade)

grader("유댕", 88)

# Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기
def bus_fare(age, pay):
    print('나이 : ', age)
    print('지불유형 : ', pay)

    if age < 8 or age >= 75:
        fare = '0'
    elif age >= 8 and age <14:
        fare = 450
    elif age >= 14 and age < 20:
        if pay == 'card':
            fare = 720
        else:
            fare = 1000
    else:
        if pay == 'card':
            fare = 1200
        else:
            fare = 1300

    print('버스요금 : ', fare, "원")

bus_fare(26, 'cash')
