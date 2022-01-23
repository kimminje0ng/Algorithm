# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = [i for i in arr if i % divisor == 0]
    return sorted(answer) if answer != [] else [-1]


# or 연산 사용한 다른 풀이 (원래 풀이가 더 직관적)
def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

'''
참고 : return에서의 and, or 연산
1) A and B
- A,B 둘 다 참   -> B 출력
- A,B 둘 다 거짓 -> A 출력
- A, B 둘 중에 하나만 참 -> 거짓인 값을 출력

2) A or B
- A,B 둘 다 참   -> A 출력
- A,B 둘 다 거짓 -> B 출력
- A, B 둘 중에 하나만 참 -> 참인 값을 출력
'''