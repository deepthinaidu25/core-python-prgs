#20.	Write a Python program to find an employee total salary  if ta = 10%, da = 15% and hra=30% of basic
basic=8000
ta_percentage=10
da_percentage=15
hra_percentage=30

ta=(ta_percentage*100)/basic
da=(da_percentage*100)/basic
hra=(hra_percentage*100)/basic

total_salary = ta+da+hra+basic
  
print("the total salary is:", total_salary)
