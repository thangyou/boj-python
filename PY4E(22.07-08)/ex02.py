# Q2. 학생들의 시험 답지를 보고 답안지와 비교하여 채점하는 함수
# -> 학생들의 점수와 등수를 출력

def grader(student,answers):
    name = [] # list()
    answer = []
    scores = []

    # 차이점?
    # for s in range(student):
        # TypeError: 'list' object cannot be interpreted as an integer
    # for s in range(len(student)):
        # len(student) 만큼 반복하고, 반복변수는 s => integer
        # s = s.split(",")
        # AttributeError: 'int' object has no attribute 'split'
    for s in student:
        s = s.split(",")
        name.append(s[0])
        answer.append(s[1])

        score = 0

        for a in answer: # 반복변수 a 는 'str'
            for i in range(len(a)):
                if int(a[i]) == answers[i]:
                    score = score + 10
            scores.append(score)
            score = 0

        for i in range(len(name)):
            name[i] = str(scores[i]) + name[i]
        name.sort(reverse=True)

    # for grade in range(1,len(s)+1):
    #     print("학생:",name,"점수:",score,grade,"등")
    for i in range(len(name)):
        print(f"학생: {name[i][2:]} 점수: {name[i][:2]}점 {i+1}등")

''' 출력 왜 ㅇㅈㄹ
학생: 80최정 점수: 80점 1등
학생: 808080이을 점수: 80점 2등
학생: 7070박병 점수: 80점 3등
학생: 정무 점수: 70점 4등
학생: 80808080김갑 점수: 70점 5등
'''


# 학생 답

s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

grader(s,a)
