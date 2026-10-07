salary = int(input("Enter the salary of the employee:"))

if(salary<=10000):
    hra = (salary*20)/100
    da = (salary*80)/100
    salary = salary + hra + da
    print(f"Salary of the employee: {salary}")

elif(salary<=20000):
    hra = (salary*25)/100
    da = (salary*90)/100
    salary = salary + hra + da
    print(f"Salary of the employee: {salary}")

elif(salary>20000):
    hra = (salary*30)/100
    da = (salary*95)/100
    salary = salary + hra + da
    print(f"Salary of the employee {salary}")
    
