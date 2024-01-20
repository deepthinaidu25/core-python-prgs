n=int(input("Enter the no of rows:"))
for i in range(1,n+1):
      print(" "*(n-i),end="")
      for j in range(1,i):
            print(chr(i-j+65),end="")
      for k in range(0,i):
            print(chr(k+65),end="")
      print()
      
