# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = list(phone_number)
    answer[0:-4] = ['*' * (len(answer) - 4)]
    return ''.join(answer)


## 좋은 풀이 : 굳이 문자열 변환을 하지 말고, *를 다 붙이고 그 다음에 4개 번호 붙이기
def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    return answer
