a = int(input())
s = "*"
h = " "
print(f"{h*(a-1)}{s}")
if a != 1:
  for i in range(2,a):
    print(f"{h*(a-i)}{s}{h*(i-1)}{h*(i-2)}{s}")
  
  print(s*(a*2-1))