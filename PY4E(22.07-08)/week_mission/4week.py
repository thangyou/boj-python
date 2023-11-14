# Q1. 숫자를 입력 받고 3자리마다 , 를 찍어주는 함수
def make_comma(number):
    number = str(number) # int를 str으로 변환
    length = len(number) # 숫자의 길이
    num_comma = length // 3 # 3으로 나눠서 찍어야하는 콤마의 개수 구하기
    if length % 3 ==0:
        num_comma = num_comma -1 # 길이가 3으로 나눠질 경우 -1

    new_number = "" # 새로운 숫자를 담을 변수 생성
    n = -1 # 인덱스를 거꾸로 가야하기 때문에 -1
    while num_comma != 0: # 콤마를 다 찍을 때까지 반복
        new_number = number[n] + new_number
        if  n % 3 == 0:
            new_number = "," + new_number
            num_comma = num_comma - 1
        n = n - 1
		# 콤마를 다 찍고 남은 앞의 숫자를 더해주면 완성
    print(number[:n+1]+new_number)

while True:
    num = int(input('숫자를 입력하세요:'))
    make_comma(num)
    if not num: break

# Q2. 특정 글자가 전체 글에서 몇 개 들어있는지 계산
# 변수에 담긴 글을 함수에 넣으면 txt 파일로 저장
f_path = "C:/Users/dbwjd/Python_Prac/test03.txt"

def cnt_word(a,b):
    cnt = 0
    f = open(f_path, 'w')
    f.write(a)
    f = open(f_path, 'r')
    while True:
        line = f.readline() # 한 줄
        line = line.strip() # 줄 끝의 개행문자 제거
        if b in line:
            cnt = cnt + 1
            print(b,'Found')
        if not line: break
    print(cnt)

    f.close()

a = '''You are the sunrise
I'll be your sunset
You be my moonlight
I'll be your sky
'''

cnt_word(a,'You')
#cnt_word(a,"YOU|I")

# Q3. 요즘 식당에 들어가면 방명록을 적게 되어있습니다.
# 어느 식당의 사장님이 여러분에게 방명록을 주면서 전화번호를
# 제대로 적었는지 검사해달라는 부탁을 했습니다.
# 아래와 같은 방명록이 있을 때 방명록을 잘 못쓴 사람의 이름과
# 잘 못된 번호를 출력하는 함수를 만들어 봅시다.
# 함수에 방명록을 넣으면 txt 파일로 저장되게 해줍니다.
# 제대로 적은 방명록의 조건은 다음과 같습니다
# 1) 010 으로 시작함
# 2) 번호가 - 로 구분이 되어 있음
# -> re.match('010-[0-9]{4}-[0-9]{4}', info[1])
# 3) -를 포함하여 길이가 13임
f_path = "C:/Users/dbwjd/Python_Prac/test04.txt"

def wrong_guest_book(guest_book):
    f = open(f_path, 'w')
    f.write(guest_book)
    f = open(f_path, 'r')
    while True:
        line = f.readline() # 한 줄
        line = line.strip() # 줄 끝의 개행문자 제거
        if not line: break
        info = line.split(',')
        if not info[1].startswith('010') or '-' not in info[1] or len(info[1]) != 13:
            print('잘못 쓴 사람:',info[0])
            print('잘못 쓴 번호:',info[1],"\n")

    f.close()

guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""
wrong_guest_book(guest_book)

##################################################

def wrong_guest_book(guest_book):
    while True:
        count = 0
        line = guest_book.count('\n') + 1
        if count >= line:
            break
        enter = guest_book.find('\n')
        x = guest_book[ : enter]
        name = x[ : 2]
        phone = x[3 : ]
        if phone.startswith('010') == False:
            print(name, phone)
        elif phone[3] or phone[8] != '-':
            print(name, phone)
        elif len(phone) != 13:
            print(name, phone)
        guest_book= guest_book.lstrip(x)
        count = count + 1

wrong_guest_book(guest_book)

# Q4. 주민등록번호의 앞 6자리는 생년월일이고 뒷자리의 시작번호는 성별을 나타냅니다.
# 주민등록번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지 출력하는 함수를 만들어 봅시다.
# 주민등록번호 조건을 만족하지 않는 수가 입력되면 "잘 못된 번호입니다"를 출력해주세요.
# 1) 주민등록번호는 6자리 이후에 -로 구분되어야 하고 길이는 -포함 14임
# 2) 뒷자리는 1,3 은 남자 2,4는 여자
# 3) 00 ~ 21로 시작할 경우 2000년 이후 출생자인지 물어 볼 것 (맞으면 o 틀리면 x)
# 4) 뒷자리 3, 4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음
def check_id(a):
    wrong_num = 0
    try:
        rrn = a.split('-')
        fr = rrn[0]
        be = rrn[1]

        print(int(fr[:2]), type(int(fr[:2])))

        if a[6] == '-' and len(a) == 14:
            if -1 < int(fr[:2]) < 22:
                aft = input('2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ')
                if aft == 'o':
                    if be.startswith('3'): gender = '남자'
                    elif be.startswith('4'): gender = '여자'
                else: # aft == 'x'
                    if be.startswith('1'): gender = '남자'
                    elif be.startswith('2'): gender = '여자'
            else:
                if be.startswith('1'): gender = '남자'
                elif be.startswith('2'): gender = '여자'
            print(fr[:2]+'년'+fr[2:4]+'월 '+gender)
        else:
            print('잘못된 번호입니다.\n올바른 번호를 넣어주세요.')
    except:
            print('잘못된 번호입니다.\n올바른 번호를 넣어주세요.')

while True:
    a = input('주민번호 : ')
    check_id(a)
    if not num: break
