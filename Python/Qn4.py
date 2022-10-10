
#allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)
def allowances(bs) :
    hra= 0.22*bs
    da=0.18*bs
    ta=0.10*bs
    return hra+da+ta

#deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)

def deductions(bs):

 if bs>8000:
        proftax=200
 else:
        proftax=150

 pf= 0.12*bs
 insurance=0.08*bs

 return proftax+pf+insurance

#netsalary = grosssalary - deductions
#grosssalary = basicsalary + allowances

def calculate_salary(bs) :
    gross_salary = bs + allowances(bs)
    net_salary = gross_salary - deductions(bs)
    print("Gross Salary= ", gross_salary)
    print("Net Salary= ", net_salary)


basic_salary = int(input("Enter your basic salary: "))
calculate_salary(basic_salary)
