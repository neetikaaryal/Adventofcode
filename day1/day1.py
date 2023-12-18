x="5sixonesix3pzhd"
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
concat(x)
with open("day1input.txt", "r") as f:
    data=f.readlines()
# print(data)
summ=0
for z in data: 
    summ=summ+concat(z)

print(summ)
    

    
