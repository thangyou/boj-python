# % formatting / str.format / f-string
# 1. 기본형식
temperature = 202
measure = 'Fahrenheit'
print('Water boils at %d degrees %s' % (temperature, measure))
print('Water boils at {} degrees {}'.format(temperature, measure))
print(f'Water boils at {temperature} degrees {measure}')
# Water boils at 202 degrees Fahrenheit

# 2. Padding, Aligning
string = 'test'
print('%10s' % (string))
print('{:>10}'.format(string))
print(f'{string:>10}')
#       test

print('%-10s' % (string))
print('{:10}'.format(string))
print(f'{string:10}')
# test

# 특정 문자로 공백 채우기
string = 'test'
print('{:*>10}'.format('test'))
print(f'{string:*>10}')
# ******test

print('{:*<10}'.format('test'))
print(f'{string:*<10}')
# test******

# 가운데 정렬
string = 'test'
print('{:^10}'.format('test'))
print(f'{string:^10}')
#   test

print('{:*^10}'.format('test'))
print(f'{string:*^10}')
# ***test***

# 3. 문자열 자르기
string = 'xylophone'
print('%-.5s' % (string))
print('{:.5}'.format(string))
print(f'{string:.5}')
# xylop

# 4. 숫자 출력
# float 로 출력 - 소수 6자리까지 표현
number = 3.141592653589793
print('%f' % (number))
print('{:f}'.format(number))
print(f'{number:f}'.format(number))
# 3.141593
print(f'{number}')
# 3.141592653589793

# 소수점 아래 2자리까지 표현
number = 3.141592653589793
print('%.2f' % (number))
print('{:.2f}'.format(number))
print(f'{number:.2f}')
# 3.14

# 5. str, repr 출력
# 객체의 __str__과 __repr__을 다양한 방식으로 문자열에 출력
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Eric", "Idle", "74")
print("%s" % (new_comedian))
print("%r" % (new_comedian))
print("{0!s}".format(new_comedian))
print("{0!r}".format(new_comedian))
print(f'{new_comedian}')
print(f'{new_comedian!r}')
# Eric Idle is 74.
# Eric Idle is 74. Surprise!

# 6. Named placeholders
# keyword를 이용하여 객체 formatting
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('%(first)s %(last)s' % data)
print('{first} {last}'.format(**data))
print('{first} {last}'.format_map(data))
# Hodor Hodor

# 7. Get item, Get attribute
# f-string의 경우 내부에서 map의 key를 입력할 때 '(작은따옴표) 사용
# 따라서 문자열은 "(큰따옴표) 사용 -> 반대도 가능
person = {'first': 'Jae', 'last': 'Hyun'}
print('{p[first]} {p[last]}'.format(p=person))
print(f"{person['first']} {person['last']}")
# Jae Hyun

# Array
data = [4, 8, 15, 16, 23, 42]
print('{d[4]} {d[5]}'.format(d=data))
print(f'{data[4]} {data[5]}')
# 23 42

# class
class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]

print('{p.type} : {p.kinds[0][name]}'.format(p=Plant()))
# tree : oak
p = Plant()
print(f"{p.type} : {p.kinds[0]['name']}")
# tree : oak

# 8. Datetime
from datetime import datetime
# datetime package - date, time, datetime, timedelta, tzinfo, timezone, ...
print('{:%Y-%m-%d %H:%M}'.format(datetime(1997, 3, 14, 13, 20)))
# 1997-03-14 13:20
date = datetime(1994,8,9,12,59)
print(f"{date:%Y-%m-%d %H:%M}")
# 1994-08-09 12:59

# 9. Parameterized format
# 인자로 값을 전달하여 formatting
# padding과 aligning 적용
p_align = '^'
p_width = '10'
string = 'test'
print('{:{align}{width}}'.format(string, align=p_align, width=p_width))
print(f'{string:{p_align}{p_width}}')
#    test

# datefime 적용
from datetime import datetime
dt = datetime(2022, 8, 17, 10, 34)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))
print(f'{dt:{"%Y-%m-%d"} {"%H:%M"}}')
#2022-08-17 10:34

# 출처 : https://codechacha.com/ko/python-string-formatting/
