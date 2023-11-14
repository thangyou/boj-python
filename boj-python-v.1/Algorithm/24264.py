# 입력값 n에 따라 반복 횟수는 n^2 (for문 2개)
# O(n^2)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''
n = int(input())
print(n**2)
print(2)