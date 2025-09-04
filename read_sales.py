import csv

sales_file = csv.reader(open('sales.csv', 'r'), delimiter=',')

header = next(sales_file)

total ={}

for rec in sales_file:
    total[rec[0]] = total.get(rec[0], 0) + float(rec[3])

print("CustomerID,Total")

for cust_id, subtotal in total.items():
    print(f"{cust_id},{subtotal:.2f}")


outfile = open('salesreportFINAL.csv', 'w')
outfile.write('CustomerID,Total\n')

for cust_id, subtotal in total.items():
    outfile.write(cust_id + ',' + f"{subtotal:.2f}" + '\n')

outfile.close()

print("Sales report written to salesreportFINAL.csv")

