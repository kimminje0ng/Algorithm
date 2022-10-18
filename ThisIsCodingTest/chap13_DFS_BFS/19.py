# https://www.acmicpc.net/problem/14888

from itertools import permutations

# 숫자 입력
n = int(input())
num_list = list(map(int, input().split()))
#print(num_list)

# 연산자 입력: +, -, x, %
oper = ['+', '-', '*', '%']
oper_num_list = list(map(int, input().split()))

oper_list = []  # 연산자 리스트
for i in range(4):
    while oper_num_list[i] >= 1:
        oper_list += oper[i]
        oper_num_list[i] -= 1
#print(oper_list)

# 1) 연산자 조합 구함. 이때 연산자 갯수는 n-1개로, n-1개만큼 조합 구함
comb_oper_list = list(permutations(oper_list, n-1))
#print(comb_oper_list)

# 2) 숫자 리스트에 연산자 조합 그대로 투입해서 계산함. 이때 최대, 최소를 구하기.
min = 1e9
max = -1e9

# 연산자 모든 조합 체크
for comb in comb_oper_list:
    #print("comb print: " + str(comb))
    left = num_list[0]

    result = 0
    for i in range(n):
        right = num_list[i+1]
        if comb[i] == '+':
            result = left + right
        elif comb[i] == '-':
            result = left - right
        elif comb[i] == '*':
            result = left * right
        elif comb[i] == '%':
            if left < 0:
                left = -left
                result = left // right
                result = -result
            else:
                result = left // right
        #print(str(left) + str(comb[i]) + str(right) + " = " +str(result))
        if i == n-2:    # 마지막 숫자
            break
        left = result
    
    if result >= max:
        max = result
    if result <= min:
        min = result
        
print(max)
print(min)
