from collections import deque
import sys
q = deque()
#push_front X: 정수 X를 덱의 앞에 넣는다.
#push_back X: 정수 X를 덱의 뒤에 넣는다.
#pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#size: 덱에 들어있는 정수의 개수를 출력한다.
#empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
#front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
i = int(sys.stdin.readline())

for _ in range(i):
    x = sys.stdin.readline().split()

    if len(x) == 2:
        if x[0] == "push_front":
            q.appendleft(int(x[1]))
        else:
            q.append(int(x[1]))
    else:
        if x[0] =="pop_front":
            if len(q) == 0:
                print(-1)
            else:
                p = q.popleft()
                print(p)
        elif x[0] =="pop_back":
            if len(q) == 0:
                print(-1)
            else:
                p = q.pop()
                print(p)
        elif x[0] =="size":
            print(len(q))
        elif x[0] =="empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)

        if x[0] =="front":
            if len(q) == 0:
                print(-1)
            else:

                print(q[0])
        elif x[0] =="back":
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])
                

