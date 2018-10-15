import sqlite3

def insertDB(db,filename,sen,sp,f1,tp,fp,fn):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("INSERT INTO performance VALUES('%s',%.2f,%.2f,%.2f,%d,%d,%d)" % (filename,sen,sp,f1,tp,fp,fn))
	conn.commit()
	conn.close()
# end function

def updateDB(db,filename,sen,sp,f1,tp,fp,fn):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("UPDATE performance  SET Sen = %.2f, Sp = %.2f, F1 = %.2f, Tp = %d, Fp = %d, Fn = %d WHERE Filename = '%s'" % (float(sen),float(sp),float(f1),tp,fp,fn,filename))
	conn.commit()
	conn.close()
# end function

def fetchDB(db,filename):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT * FROM performance WHERE Filename = '%s'" % filename)
	data = c.fetchone()
	
	if(data):
		f1 = data[3]
		conn.close()
		return f1
	else:
		return -1
# end function
def performanceDB(db):
	conn = sqlite3.connect(db)
	c = conn.cursor()
	c.execute("SELECT AVG(Sen), AVG(Sp), AVG(F1) FROM performance")
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

# insertDB("BaEV",100.0, 90.0, 95.0, 14.0, 3.0, 0.0)
# res = fetchDB('BEfdV')
# print(res)
# updateDB("BaEV",100.0, 80.0, 90.0, 14.0, 3.0, 3.0)
# print(performanceDB())