# 반복횟수 (n - 1) * n = n^2 - 1 -> n^2
# O(n^2)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    # 등차수열의 합
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
'''
n = int(input())
print(int((n - 1) * n / 2))
print(2)