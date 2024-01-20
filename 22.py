#22.	Write a Python program to find to find an employee net salary

basic = float(input("Enter the basic salary: "))
ta = float(input("Enter the transport allowance: "))
da = float(input("Enter the dearness allowance: "))
hra = float(input("Enter the house rent allowance: "))
it = float(input("Enter the income tax: "))
pf = float(input("Enter the provident fund: "))
lic = float(input("Enter the life insurance premium: "))


gross_salary = basic + ta + da + hra


total_deductions = it + pf + lic


net_salary = gross_salary - total_deductions


print("Gross Salary:", gross_salary)
print("Total Deductions:", total_deductions)
print("Net Salary:", net_salary)
