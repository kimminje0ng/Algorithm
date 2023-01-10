H, M = map(int, input().split())
C = int(input())

M += C

while True:
    if M >= 60:
        H += 1
        M -= 60
    else:
        break

if H >= 24:
    dis = H - 24
    H = dis

print(str(H) + " " + str(M))