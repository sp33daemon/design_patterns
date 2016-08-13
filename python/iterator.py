def month_name(number):

	list_of_month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
	iterator =  zip(range(number),list_of_month)

	for position, monthname in iterator:
		yield monthname


val = month_name(4)
print(type(val))

for month in val:
	print("{}".format(month))
