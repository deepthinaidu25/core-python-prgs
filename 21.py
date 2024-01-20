#21.	Write a Python program to find an employee net salary if basic=10000, ta=700, da=1200, hra=3000,  it=1000, pf=500 and lic=800
basic=10000
ta=700
da=1200
hra=3000
it=1000
pf=500
lic=800
gross_salary=basic+ta+da+hra
total_deductions=it+pf+lic
net_salary=gross_salary-total_deductions
print("the total salary of an employees is:",net_salary)
