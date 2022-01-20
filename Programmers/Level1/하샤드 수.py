# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True

    arr = list(map(int,str(x)))  # int to list
    if x % sum(arr) != 0:
        answer = False

    return answer

## 한 줄로 줄여보기
def solution(x):
    return x % sum(list(map(int,str(x)))) == 0  # int to list


## 좋은 풀이
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0  # 위 풀이랑 같은 의미인데 for문으로 표현함.