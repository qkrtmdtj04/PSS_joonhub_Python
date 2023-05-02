t,m,s = map(int,input().split())
i = int(input())

i += t*3600 + m*60 + s

t_i = (i // 3600) % 24
m_i = (i % 3600) // 60
s_i = (i % 3600) % 60


print(t_i,m_i,s_i)