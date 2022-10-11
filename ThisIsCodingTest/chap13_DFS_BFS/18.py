# https://school.programmers.co.kr/learn/courses/30/lessons/60058 

# 괄호 개수 같으면, 균형잡힌 괄호 문자열
# 괄호 짝도 맞으면, 올바른 괄호 문자열

# 균형잡힌 문자열의 index
def check_balanced_index(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i 

# 올바른 문자열 체크
def check_proper(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def solution(p):
    answer = ''
    if p == '': # 빈 문자열
        return answer
    
    index = check_balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if check_proper(u):
        answer = u + solution(v)    
        
    return answer