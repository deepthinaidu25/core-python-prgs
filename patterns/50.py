num=int(input("Enter the no of rows:"))
for i in range(1,num+1):
      print("  "*(i-1),end="")
      for j in range(0,num+1-i):
            print(2*num+1-2*i,end=" ")
      for k in range(1,num+1-i):
            print(2*num+1-2*i,end=" ")
      print()
