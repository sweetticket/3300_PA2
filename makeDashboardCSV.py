import csv
import sys
import pandas


def removeDups(lst):
    newlst = []
    for i in lst:
        if i not in newlst:
            newlst.append(i)
    newlst.sort()
    return newlst


colnames = ['company_permalink','company_name','company_category_list','company_market','company_country_code',
            'company_state_code','company_region','company_city','acquirer_permalink','acquirer_name',
            'acquirer_category_list','acquirer_market','acquirer_country_code','acquirer_state_code',
            'acquirer_region','acquirer_city','acquired_at','acquired_month','acquired_quarter','acquired_year',
            'price_amount','price_currency_code']
data = pandas.read_csv('filteredData.csv', names=colnames)
years = list(data.acquired_year)
markets = list(data.company_market)

labels = ['year', 'companies_acquired'];
years_col = removeDups(years)

# add each market category to labels
for i in removeDups(markets):
    labels.append(i)

# create a threshold
THRESHOLD = 75

# get input and output files
f_reader = open('CrunchBase_Acquisitions.csv', 'rU')
f_writer = open('dashboard.csv','wt')

# clear output file
f_writer.truncate()

# setup reader and writer
reader = csv.reader(f_reader, quotechar = '"', delimiter = ',')
writer = csv.writer(f_writer)


# header
writer.writerow(labels)

for year in years_col:
    row = [0]*len(labels)
    row[0] = year
    for i in range(0, len(years)):
        if year == years[i]:
            row[1] = row[1] + 1
    for i in range(0, len(markets)):
        if markets[i] in labels and year == years[i]:
            ind = labels.index(markets[i])
            row[ind] = row[ind] + 1
    writer.writerow(row)


# iteration
#try:
#	for row in reader:
#		country = row[4]
#		category = row[2]
#		if country == 'USA' and len(category) > 0:
#				writer.writerow(row)
#				print category
#finally:
#    f_reader.close()
#    f_writer.close()