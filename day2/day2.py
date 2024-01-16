x="sevenine"
nums=['one','two','three','four','five','six','seven','eight','nine']

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
    #print(ans)
    return ans

def word_to_num(word):
    for i in nums:
        word=word.replace(i,str(nums.index(i)+1))
    num=concat(word)
    return num
print(word_to_num(x))



# with open("day2input.txt",'r') as f:
#     data=f.readlines()
#     print(data[0],data[-1])
    
# summ=0
# for line in data:
#     ans=word_to_num(line)
#     summ=summ+ans
# print(summ)

#     for i in y:
#         new_line=new_line.replace(i,str(y.index(i)+1))
#     # print(new_line)
#     summ=summ+concat(new_line)

# print(summ)

    



