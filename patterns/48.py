num=int(input("Enter the no of rows:"))
for i in range(1,num+1):
      print("  "*(i-1),end="")
      for j in range(1,num+2-i):
            print("*",end=" ")
      for k in range(1,num+1-i):
            print("*",end=" ")
      print()
