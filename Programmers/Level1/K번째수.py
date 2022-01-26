# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1 : commands[i][1]])[commands[i][2]-1])
    return answer

# 다른 풀이
def solution(array, commands):
    answer = []
    for i,j,k in commands:  # 한 번에 읽어올 수 있음
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

# 좋은 풀이
def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands] 

# 좋은 풀이 2
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))