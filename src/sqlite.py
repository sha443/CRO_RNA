import sqlite3
#-----------------------------------------------------------------------------------------
# Database opeation
#-----------------------------------------------------------------------------------------
db = "../data/database/rsppk.db"

def insertDB(table,filename,sen,sp,f1,tp,fp,fn,time,ene):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("INSERT INTO "+table+" VALUES('%s',%.2f,%.2f,%.2f,%d,%d,%d,%.2f,%.2f)" % (filename,sen,sp,f1,tp,fp,fn,time,ene))
	conn.commit()
	conn.close()
# end function

def updateDB(table,filename,sen,sp,f1,tp,fp,fn,time,ene):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("UPDATE "+table+"   SET Sen = %.2f, Sp = %.2f, F1 = %.2f, Tp = %d, Fp = %d, Fn = %d, ET= %.2f, Ene= %.2f WHERE Filename = '%s'" % (float(sen),float(sp),float(f1),tp,fp,fn,float(time),float(ene),filename))
	conn.commit()
	conn.close()
# end function

def fetchDB(table,filename):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT * FROM "+table+"  WHERE Filename = '%s'" % filename)
	data = c.fetchone()
	
	if(data):
		f1 = data[3]
		conn.close()
		return f1
	else:
		return -1
# end function
def performanceDB(table):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT AVG(Sen), AVG(Sp), AVG(F1) FROM "+table)
	data = c.fetchone()
	
	if(data):
		sen = data[0]
		sp = data[1]
		f1 = data[2]
		conn.close()
		return sen,sp,f1
	else:
		return "No records found!"
# end function
def printTable(table):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT * FROM "+table)
	for row in c:
		for items in row:
			print(items,end="\t")
		# endfor
		print("")
	# endfor

#-----------------------------------------------------------------------------------------
# Database processing area
#-----------------------------------------------------------------------------------------
def helperDB(table,filename,sen,sp,f1,tp,fp,fn,time,ene):
	res = fetchDB(table,filename)
	if(res==-1):
		# No entry, insertDB
		insertDB(table,filename,sen,sp,f1,tp,fp,fn,time,ene)
	else:
		# Check if we have a better output
		if(res<f1):
			updateDB(table,filename,sen,sp,f1,tp,fp,fn,time,ene)
		# enfif
	# endif
	print("---------------------------------------------------------------")
	print("Average Performance:")
	print(performanceDB(table))
	# printTable(table)
# end function

#-----------------------------------------------------------------------------------------
# Test
#-----------------------------------------------------------------------------------------# insertDB("BaEV",100.0, 90.0, 95.0, 14.0, 3.0, 0.0)
# res = fetchDB('BEfdV')
# print(res)
# insertDB("cro","BaEV",100.0, 80.0, 90.0, 14.0, 3.0, 3.0,11.3,-33.5)
# updateDB("cro","BaEV",100.0, 80.0, 90.0, 14.0, 3.0, 3.0,11.3,-2.5)
# print(performanceDB("cro"))