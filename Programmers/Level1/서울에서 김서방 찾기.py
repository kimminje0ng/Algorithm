# 

def solution(seoul):
    for index, name in enumerate(seoul):
        if name == 'Kim':
            answer = '김서방은 ' + str(index) + '에 있다'
    return answer

# 다른 풀이
def solution(seoul):
    answer = '김서방은 ' + str(seoul.index('Kim')) + '에 있다'
    return answer

# format 사용
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))