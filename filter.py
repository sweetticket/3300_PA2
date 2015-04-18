import csv
import sys

# create a threshold
THRESHOLD = 75

# get input and output files
f_reader = open('CrunchBase_Acquisitions.csv', 'rU')
f_writer = open('filteredData.csv','wt')

# clear output file
f_writer.truncate()

# setup reader and writer
reader = csv.reader(f_reader, quotechar = '"', delimiter = ',')
writer = csv.writer(f_writer)

# header
writer.writerow(['company_permalink',
	'company_name',
	'company_category_list',
	'company_market',
	'company_country_code',
	'company_state_code',
	'company_region',
	'company_city',
	'acquirer_permalink',
	'acquirer_name',
	'acquirer_category_list',
	'acquirer_market',
	'acquirer_country_code',
	'acquirer_state_code',
	'acquirer_region',
	'acquirer_city',
	'acquired_at',
	'acquired_month',
	'acquired_quarter',
	'acquired_year',
	'price_amount',
	'price_currency_code']);

# iteration
try:
	for row in reader:
		country = row[4]
		category = row[2]
		if country == 'USA' and len(category) > 0:
				writer.writerow(row)
				print category
finally:
    f_reader.close()
    f_writer.close()