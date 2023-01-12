N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, input().split())))
# print(info)

for i in range(N):
    score = 0
    for j in range(N):
        # 덩치가 더 큰 경우(키, 몸무게 모두 큰 경우)
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            score += 1
    # 덩치 등수 = 자신보다 큰 덩치의 사람 수+1
    info[i].append(score+1)

for i in range(N):
    print(info[i][2],end=" ")

