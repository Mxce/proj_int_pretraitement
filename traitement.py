import pandas

#CHANGE THESE:
path = 'JC-201802-citibike-tripdata.csv'
outputpath = 'testcsv.csv'
datecolumns_list = ['starttime','stoptime']

#Dataframe initialization from csv
df = pandas.read_csv(path, parse_dates = datecolumns_list)

print('current head of file: ' + str(df.head()))

def process_dates(row, datecol):
	'''takes a row and column name and returns in a tuple the hour, dayofweek,
	day number and month from the date contained in the row[datecol] cell
	'''
	
	st = row[datecol]
	return (st.hour, st.dayofweek, st.day, st.month)
	

def addcolumns(df, columnnames_list, procfunct):
	'''this function adds columns to df.
	
	df : dataframe to be modified (effets de bord bonjour)
	columnnames_list : list containing the names of the columns to be added
	procfunct : function accepting a row as an argument and returning
		the values of the columns to be added in the same order as columnnames_list,
		in a tuple. Tuple size must be equal to len(columnnames_list)
	'''
	
	df[columnnames_list]= df.apply(lambda row: procfunct(row), axis=1, result_type= 'expand')

'''df[['starthour','startdayofweek','startday','startmonth']]= df.apply(lambda row: ftest(row,'starttime'), axis = 1, result_type = 'expand')

df[['
stophour','stopdayofweek','stopday','stopmonth']]= df.apply(lambda row: ftest(row,'stoptime'), axis = 1, result_type = 'expand')'''

addcolumns(df, ['starthour','startdayofweek','startday','startmonth'], lambda row: process_dates(row, 'starttime'))

addcolumns(df, ['stophour','stopdayofweek','stopday','stopmonth'], lambda row: process_dates(row, 'stoptime'))



print('new head of file: ' + str(df.head()))
df.to_csv(outputpath)

