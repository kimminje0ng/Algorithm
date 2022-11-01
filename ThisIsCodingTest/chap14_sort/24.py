# https://www.acmicpc.net/problem/18310

n = int(input())
home_list = sorted(list(map(int, input().split())))

print(home_list[(len(home_list)-1)//2])

# 아래는 시간 초과 코드
# min = 1e9
# for i in range(n):
#     sum = 0
#     for j in range(n):
#         if j < i:
#             sum += home_list[i] - home_list[j]
#         if j > i:
#             sum += home_list[j] - home_list[i]
#     if sum < min:
#         min = sum
#         min_home_num = i

# print(home_list[min_home_num])