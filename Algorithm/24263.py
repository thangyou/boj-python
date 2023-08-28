# 입력값 n에 따라 반복 횟수가 n만큼 증가
# O(n)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        sum <- sum + A[i]; # 코드1
    return sum;
}
'''
n = int(input())
print(n)
print(1)  # 선형복잡도 = 1차식
