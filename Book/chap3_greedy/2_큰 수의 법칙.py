'''간단하게 구현'''
n, m, k = map(int, input().split())  # n: 입력할 숫자 총 갯수, m: 넣을 숫자 갯수, k: 최대 반복 갯수
data = list(map(int, input().split()))
data.sort()

result = 0
while True:
    for j in range(k):  # 최대 반복 횟수
        if m == 0:  # 체크는 맨 앞에서 해야함
            break
        result += data[-1]  # 가장 큰 수 
        m -= 1
    if m <= 0:
        break
    result += data[-2]  # 두 번째로 큰 수
    m -= 1

print(result)


'''효율적으로 구현 : 반복되는 배열을 하나로 묶어서 처리. ex) (6+6+6+5)+(6+6+6+5)+...'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

# 가장 큰 수 더하는 횟수 : 넣는 갯수 // (최대반복+1) * 최대반복 + 넣는 갯수 % (최대반복+1)
#                                외부갯수          * 내부갯수 
count = int(m / (k+1))*k + m % (k+1) 

result = 0
result += data[-1] * count
result += data[-2] * (m - count)

print(result)


''' [input]
5 8 3
2 4 5 4 6
'''