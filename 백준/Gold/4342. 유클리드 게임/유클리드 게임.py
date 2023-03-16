import sys

def ucled(a1, b1): # 리스트 형태로 두 수를 받는다
    if a1 % b1 == 0:
        return True
    elif a1 - b1 < b1:
        return False if ucled(b1,a1 - b1) else True
    else:
        return True


while True: # 두 수 받고 이어서 하는 게임 제작
    a,b = map(int, sys.stdin.readline().split())
    if a == 0:
        break
    elif a < b:
        a,b = b,a
    if ucled(a,b):
        print("A wins")
    else:
        print("B wins")