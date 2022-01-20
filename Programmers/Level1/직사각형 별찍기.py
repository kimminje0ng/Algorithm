# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))

for i in range(b):  # 굳이 여기엔 왜 for문을 썼을까..
    print("*" * a)


## 추천 방법
print("*" * a + "\n") * b