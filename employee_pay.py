import csv

employee_file = csv.reader(open('Employee_data.csv', 'r'), delimiter=',')

next(employee_file)

for rec in employee_file:
    print(f"First Name: {rec[1]}")
    #print(f"Last Name: {rec[2]}")
    print(f"Salary: ${float(rec[3]):,.2f}")

    bonus = int(rec[3]) * float(rec[7])
    print(f"Bonus amount: {bonus:,.2f}")

    total_pay = int(rec[3]) + bonus

    print(f"Total pay: {total_pay:,.2f}")

    input()