# https://programmers.co.kr/learn/courses/30/lessons/12937

def solution(num):
    if num % 2:  # %2가 0이면->False->else문 실행->짝수
        return 'Odd'
    else:
        return 'Even'

## 이것도 가능
def solution(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

## 좋은 풀이
def solution(num):
    return "Even" if num % 2 == 0 else "Odd"