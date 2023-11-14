# 파일 읽고 쓰기

# 파일 쓰기
# 1. 파일을 사용한 입력
#f = open("C:/Users/dbwjd/Python_Prac/test01.txt", 'w')
#for i in range(1,11):
#    data = "%d번째 줄입니다.\n" % i
#    f.write(data)

# 2. 키보드를 사용한 입력
#while True:
#    data = input()
#    if not data: break
#    print(data)

# 파일에 새로운 내용 추가하기
#f = open("C:/Users/dbwjd/Python_Prac/test02.txt", 'a')
#for i in range(2,3):
#    data = "Life is too short, you need python\n"
#    f.write(data)

# 파일 읽기
f = open("C:/Users/dbwjd/Python_Prac/test03.txt", 'r')
#data = f.read() # 파일 전체
#print(data)
while True:
    line = f.readline() # 한 줄
    line = line.strip() # 줄 끝의 개행문자 제거
    if not line: break
    print(line)

# 파일명 입력받아서 해당 파일 열기
#fname = input('Enter the file name:')
#f = open("C:/Users/dbwjd/Python_Prac/"+fname)
#cnt = 0
#for line in f:
#    cnt = cnt + 1
#print('There were', cnt, 'lines in', fname)

f.close()

# 파일 생성과 쓰기, 자동으로 close
#with open("C:/Users/dbwjd/Python_Prac/test02.txt", 'w') as f:
#    f.write("Life is too short, you need python")
