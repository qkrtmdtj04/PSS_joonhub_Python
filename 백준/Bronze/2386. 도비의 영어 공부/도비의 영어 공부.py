while True:
    s = input()
    if s == '#':
        break
    c = s[0]
    c1 = c.upper()
    c2 = c.lower()
    p = s.count(c1) + s.count(c2) -1
    print(c, p)