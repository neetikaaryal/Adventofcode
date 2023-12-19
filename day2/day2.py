x="rxzgrqeightseven18five4txv"
y=['one','two','three','four','five','six','seven','eight','nine']
def concat(y:str):
    for i in y:
        if i.isdigit():
            first=i
            break

    for j in y[::-1]:
        if j.isdigit():
            last=j
            break
    ans=first+last
    ans=int(ans)
    # print(ans)
    return ans


with open("day1input.txt",'r') as f:
    data=f.readlines()
summ=0
for line in data:
    new_line=line
    for i in y:
        new_line=new_line.replace(i,str(y.index(i)+1))
    print(new_line)
    summ=summ+concat(new_line)
print(summ)

    



