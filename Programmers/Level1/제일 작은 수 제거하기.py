# https://programmers.co.kr/learn/courses/30/lessons/12935

# [처음 풀이] => [3,2,1,1,1]일 때 해결 불가능
# 최소값의 index 구함 -> 해당 index를 pop함
def solution(arr):
    if len(arr) <= 1:  # len==0일 수도 있으므로 <= 써야함
        return [-1]
    else:
        arr.pop(arr.index(min(arr)))

    return arr

# 다른 풀이 => [3,2,1,1,1] 해결 But arr이 길어질수록 별로인 코드라고 함..
def solution(arr):
    if len(arr) <= 1:
        return [-1]
    else:
        return [i for i in arr if i > min(arr)]