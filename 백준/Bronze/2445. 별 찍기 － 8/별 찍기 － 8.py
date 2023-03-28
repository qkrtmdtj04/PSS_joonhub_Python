a = int(input())
s = "*"
h = " "


for i in range(1,a+1):
  print(f"{s*(i)}{h*(a-i)}{h*(a-i)}{s*(i)}")
for i in range(1,a+1):
  print(f"{s*(a-i)}{h*i}{h*i}{s*(a-i)}")