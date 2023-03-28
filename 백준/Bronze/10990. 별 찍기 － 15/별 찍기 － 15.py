a = int(input())
s = "*"
h = " "
print(f"{h*(a-1)}{s}")
for i in range(2,a+1):
  print(f"{h*(a-i)}{s}{h*(i-1)}{h*(i-2)}{s}")