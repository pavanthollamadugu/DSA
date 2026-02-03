numday=int(input("how many days temperature"))
total =0 
temp=[]
for i in range(numday):
    nextday = int(input("day"+str(i+1)+"'s high temp"))
    temp.append(nextday)
    total+=temp[i]
avg = round(total/numday,2)
print("\naverage = "+str(avg))
above = 0 
for i in temp:
    if i >avg:
        above+=1
print(str(above)+"days above average")
