
def count_love(str,l,o,v,e):
    L = l + str.count("L")
    O = o + str.count("O")
    V = v + str.count("V")
    E = e + str.count("E")

    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100




s = input()
ll = s.count("L")
oo = s.count("O")
vv = s.count("V")
ee = s.count("E")


n = int(input())
t = [input() for _ in range(n)]
t_c = [0 for _ in range(n)]
t.sort()
for i in range(len(t)):
    t_c[i] = count_love(t[i],ll,oo,vv,ee)

print(t[t_c.index(max(t_c))])