'''
Q4. 날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수
조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.

HINT : 특정 원소의 위치를 찾는 방법
a = [1,2,3,4]
a.index(1)
0
'''
# 객체 사용
import datetime
start_date = datetime.datetime.today()
d_day = 100
target_date = start_date + datetime.timedelta(d_day)

print(f"start date : {start_date}")
print(f"d-day : {d_day}")
print(f"target_date : {target_date}")

# 내가 풀어
def after_100(m,d,wd):


    print(m,"월",d,"일",wd,"요일부터 100일 뒤는")

after_100(6,21,'월')
