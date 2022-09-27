# https://school.programmers.co.kr/learn/courses/30/lessons/60061

'''
build_frame: 기둥,보의 설치 및 삭제가 담긴 2차원 배열. [x,y,a,b]
  - x, y: 기둥, 보를 설치 또는 삭제할 교차점의 좌표. [가로,세로]
  - a: 설치 또는 삭제할 구조물의 종류. 0(기둥), 1(보)
  - b: 구조물을 설치 or 삭제할 지. 0(삭제), 1(설치)
answer = [x, y, build_type]
'''

def IsPossible(answer):
    for frame in answer:
        x, y, build_type = frame
        if build_type == 0:     # 기둥
            if y == 0:                  # 바닥에 이어짐
                continue
            elif [x-1, y, 1] in answer: # 왼쪽에 보
                continue
            elif [x, y, 1] in answer:   # 오른쪽에 보
                continue
            elif [x, y-1, 0] in answer: # 아래에 기둥
                continue
            else:
                return False                
        elif build_type == 1:   # 보
            if [x, y-1, 0] in answer:                               # 왼쪽 기둥
                continue
            elif [x+1, y-1, 0] in answer:                           # 오른쪽 기둥
                continue
            elif [x-1, y, 1] in answer and [x+1, y, 1] in answer:   # 양쪽 보
                continue
            else:
                return False   
    return True


def solution(n, build_frame):
    answer = []   # [x,y,a(기둥0, 보1)]
    
    for frame in build_frame:
        x, y, build_type, install = frame
        if install == 1:    # 설치
            answer.append([x, y, build_type])
            if IsPossible(answer) == False:
                answer.remove([x, y, build_type])
        elif install == 0:  # 삭제
            answer.remove([x, y, build_type])
            if IsPossible(answer) == False:
                answer.append([x, y, build_type])
    return sorted(answer)
