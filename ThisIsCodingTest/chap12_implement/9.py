# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s) # 최소값 저장

    for length in range(1, len(s)//2+1): # len//2+1 주의
        cnt = 1
        final = ""
        before = s[0:length]
        for i in range(length, len(s), length):
            after = s[i:i+length]
            if before == after:
                cnt += 1
            else:
                if cnt >= 2:
                    final += str(cnt)
                final += before
                cnt = 1
                before = after  # 초기화
        if cnt >= 2:    # 남은 단어
            final += str(cnt)
        final += before
        
        if len(final) < answer: # min값 변경
            answer = len(final)
        
    return answer