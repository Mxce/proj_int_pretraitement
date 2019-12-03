import pandas

#CHANGE THESE:
path = 'JC-201802-citibike-tripdata.csv'
outputpath = 'testcsv.csv'


df = pandas.read_csv(path, parse_dates = ['starttime','stoptime'])

print(df.head())

def ftest(row, datecol):
	st = row[datecol]
	return (st.hour, st.dayofweek, st.day, st.month)
	

df[['starthour','startdayofweek','startday','startmonth']]= df.apply(lambda row: ftest(row,'starttime'), axis = 1, result_type = 'expand')
print(df['starthour'][4])
print(df['startdayofweek'][4])

df[['stophour','stopdayofweek','stopday','stopmonth']]= df.apply(lambda row: ftest(row,'stoptime'), axis = 1, result_type = 'expand')

df.to_csv(outputpath)

