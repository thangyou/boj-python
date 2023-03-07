'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

출력
입력으로 주어진 숫자 N개의 합을 출력한다.

sum(iterable, start = 0)
첫번째 인자 : iterable하고 숫자데이터가 들어간 객체, 변수
두번째 인자 : 처음으로 또 더해줄 숫자
반환 : iterable의 합 + start 값

list(map(함수, 리스트))
리스트의 요소를 지정된 함수로 처리해주는 함수
'''
# 1. sum 함수 사용
# num = input() # num 사용 X
# print(sum(map(int,input())))
# n개의 숫자가 공백 없는 문자열인 점을 이용
# map 함수로 각 자리의 수를 int로 처리 후 sum 함수

# 2. for문 사용
cnt = int(input())
num = input() # 사용자가 입력한 값은 문자열로 취급
sum = 0
for i in range(cnt): # 0 ~ cnt-1
    sum += int(num[i])
print(sum)
