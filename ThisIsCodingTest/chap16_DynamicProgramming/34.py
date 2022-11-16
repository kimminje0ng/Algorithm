# https://www.acmicpc.net/problem/18353
# LIS(최장길이부분수열)로 푸는 문제

n = int(input())
info = list(map(int, input().split()))
info.reverse()
#print(info)

DP = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if info[j] < info[i]:
            DP[i] = max(DP[j]+1, DP[i]) # 기존 값보다 큰 +1 값만 저장함.

print(n - max(DP))
