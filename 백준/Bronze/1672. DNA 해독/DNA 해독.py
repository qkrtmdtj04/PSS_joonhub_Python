s = int(input())
i_s = input()
i = []
for j in range(len(i_s)):
    i.append(i_s[j])

while len(i) != 1:

    if (i[s-1] == "A" and i[s-2] in ["A","C"]) or (i[s-2] == "A" and i[s-1] == "C") or (i[s-1] == "G" and i[s-2] == "T") or (i[s-1] == "T" and i[s-2] == "G"): 
        del i[-1]
        del i[-1]
        i.append("A")
        s -=1
    elif (i[s-1] == "G" and i[s-2] == "G") or (i[s-1] == "A" and i[s-2] == "T") or (i[s-1] == "T" and i[s-2] == "A") or (i[s-1] == "C" and i[s-2] == "T") or (i[s-1] == "T" and i[s-2] == "C"): 
        del i[-1]
        del i[-1]
        i.append("G")
        s -=1
    elif (i[s-1] == "C" and i[s-2] == "C") or (i[s-1] == "A" and i[s-2] == "G") or (i[s-1] == "G" and i[s-2] == "A"): 
        del i[-1]
        del i[-1]
        i.append("C")
        s -=1
    elif (i[s-1] == "T" and i[s-2] == "T") or (i[s-1] == "C" and i[s-2] == "G") or (i[s-1] == "G" and i[s-2] == "C"): 
        del i[-1]
        del i[-1]
        i.append("T")
        s -=1
print(i[0])