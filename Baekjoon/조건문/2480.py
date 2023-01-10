a, b, c = map(int, input().split())

reward = 0
if a==b==c:
    reward = 10000 + a * 1000
elif a==b or b==c:
    reward = 1000 + b*100
elif a==c:
    reward = 1000 + a*100
else:
    max_num = max(a, b, c)
    reward = max_num * 100

print(reward)