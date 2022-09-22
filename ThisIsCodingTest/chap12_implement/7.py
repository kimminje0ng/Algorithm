# https://www.acmicpc.net/problem/18406

n = input()
len = len(n)

sum = 0
for i in range(len//2):
    sum += int(n[i])
for i in range(len//2, len):
    sum -= int(n[i])

if sum == 0:
    print("LUCKY")
else:
    print("READY")