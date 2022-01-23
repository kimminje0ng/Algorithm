# https://programmers.co.kr/learn/courses/30/lessons/12906

# 주의 : 배열끼리 합칠 때에는 extend(리스트), 원소만 추가할 때에는 append(원소)
# 참고 : 슬라이싱([:]) 할 때에는 indexing 범위 넘어도 오류뜨지 않음!

def solution(arr):
    answer = [arr[0]]  # 0번째
    answer.extend([arr[i] for i in range(1,len(arr)) if arr[i-1] != arr[i]])  # [1]~[마지막]까지
    return answer

# 더 간략하게 만든 풀이
def solution(arr):
    return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i+1:i+2]]  # 슬라이싱은 []로 return되므로, [arr[i]]로 반환해야함

# 좋은 풀이
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]:  # 직전값이 지금 값과 같으면 패스 => answer[-1]로 해버리면, answer이 빈배열일 때 문제 생김
            continue 
        answer.append(i)
    return answer

