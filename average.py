List=[90,80,90,40,50,60]
avg=0
sum=0
for x in range(len(List)):
    sum=sum+List[x]
print('Sum of list values: ',sum)
avg=sum/len(List)
print('Average of List values: ',avg)