# 1 ~ n까지 반복 횟수 = 3
# O(n^3)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''
n = int(input())
print(n**3)
print(3)