n = [int(input()) for _ in range(3)]


if sum(n) == 180:
    if n[0] == 60 and n[1] == 60 and n[2] == 60:
        print("Equilateral")
    elif n[0] == n[1] or n[0] == n[2] or n[2] == n[1]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")

