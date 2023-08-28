import datetime
# 1
# now() 함수를 사용해 지금의 날짜, 시간을 출력
print(str(datetime.datetime.now())[:10])

# 2
# today() 함수를 사용해 오늘의 날짜, 시간을 출력
print(str(datetime.datetime.today())[:10])

# 3 
d = datetime.datetime.today()
print(d.isoformat())  # 'YYYY-MM-DD'형태의 문자열로 반환하는 메서드