a  = {3:"ABC",
      4:"DEF",
      5:"GHI",
      6:"JKL",
      7:"MNO",
      8:"PQRS",
      9:"TUV",
      10:"WXYZ"
     }
s = 0

i = input()
for i_t in range(len(i)):
    for k,v in a.items():
        if i[i_t] in v:
            s += k

print(s)