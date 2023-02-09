'''
5단계 : 함수
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
입력 - 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
출력 - 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
(설명 https://www.acmicpc.net/board/view/25689)
'''

def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i))) # 숫자를 분리할 때는 str함수를 이용해서 문자열로 변환
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수
            # 1~9: 길이가 1인 등차수열
            # 10~99: 길이가 2이고 공차는 양수 또는 음수인 등차수열
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))
