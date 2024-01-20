a=[]
for i in range(1,101):
       if i % 2 == 1:
            a.append(i)
sum=0
for j in a:
      sum+=j
print("the sum of all odd numbers equal ", sum)
