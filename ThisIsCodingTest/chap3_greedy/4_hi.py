n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

count = int(m / (k+1))*k + m % (k+1) # 가장 큰 수 더하는 횟수 : 넣는 갯수//(최대반복+1)*최대반복[외부갯수*내부갯수] + 넣는 갯수%(최대반복+1)

result = 0
result += data[-1] * count
result += data[-2] * (m - count)

print(result)
