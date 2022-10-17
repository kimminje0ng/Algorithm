# https://www.acmicpc.net/problem/10825

# 1) 국어 점수 감소
# 2) 영어 점수 증가
# 3) 수학 점수 감소
# 4) 이름순 사전

# 도현이네 반 학생 수
n = int(input())
info = [] * n

for _ in range(n):
    name, korean, english, math = input().split()
    info.append([name, int(korean), int(english), int(math)])
#print(info)

info.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for person in info:
    print(person[0])