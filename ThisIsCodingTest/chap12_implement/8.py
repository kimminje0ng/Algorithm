data = input()  # 변수명 str 예약됨
result = []
sum = 0

for c in data:
    if c.isalpha():
    #if c >= 'A' and c <= 'Z':
        result.append(c)
    else:
        sum += int(c)

# result = sorted(result)   # 새로 할당해서 sorted 저장
result.sort()               # 기존 정렬 sort

if sum != 0:
    result.append(str(sum))
print(''.join(result))