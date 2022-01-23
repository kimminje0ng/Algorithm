# https://programmers.co.kr/learn/courses/30/lessons/12925

def solution(s):
    answer = int(s)
    return answer


# 만약 변환 함수가 없다면?
def solution(s):
    answer = 0
    # enumerate() : index랑 값을 tuple형태로 반환하면서 for문 돌림
    for index, num in enumerate(s[::-1]):
        if num == '-':
            answer *= -1
        elif num == '+':
            continue
        else:
            answer += int(num) * 10**index
    return answer
    
    