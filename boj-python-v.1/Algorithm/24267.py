# 반복횟수 (n - 2) * (n - 1) * n -> n^3
# O(n^3)
'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
'''
# 1 ~ n까지의 숫자 중 3가지를 뽑아 중복 없이 크기 순 작성
# nC3 = n! / (n-3)!3! = ((n-2)*(n-1)*n) / 6
n = int(input())
print(int((n * (n - 1) * (n - 2)) / 6))
print(3)