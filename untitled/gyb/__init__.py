import pymysql

pymysql.install_as_MySQLdb()

db=pymysql.connect("192.168.216.130","root","gyb414723","test")

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print("mysql Database version:%s"%data)

db.close()