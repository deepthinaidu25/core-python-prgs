#23.	Write a Python program to find an employee net salary if ta=5%, da=10%, hra=20%, pf=5%, it=30% and lic=8% of basic
basic=float(input("enter the basic salary:"))
ta_percentage=5
da_percentage=10
hra_percentage=20
pf_percentage=5
it_percentage=30
lic_percentage=8

ta=(ta_percentage*100)/basic
da=(da_percentage*100)/basic
hra=(hra_percentage*100)/basic
pf=(pf_percentage*100)/basic
it=(it_percentage*100)/basic
lic=(lic_percentage*100)/basic

gross_salary=basic+ta+da+hra
total_deductions=pf+it+lic
net_salary=gross_salary-total_deductions
print("the net salary is:", net_salary)
