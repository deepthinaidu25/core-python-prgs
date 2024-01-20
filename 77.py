#77.	Write a Python program to print the below series up to 100by using the do-while statement
#1,3,6,8,11,13,16 …
num=1
increment=2

while True:
      print(num)
      num+=increment
      if num>100:
            break
      increment=3 if increment==2 else 2
    
