import csv

#customers = open('customers.csv', 'r')

csv_file = csv.reader(open('customers.csv', 'r'), delimiter=',')

outfile = open('customer_country.csv', 'w')

outfile.write('Full Name,Country\n')
              

next(csv_file)
for row in csv_file:
    name = row[1] + '' + row[2]
    country = row[4]

    outfile.write(name + ',' + country + '\n')

outfile.close()
