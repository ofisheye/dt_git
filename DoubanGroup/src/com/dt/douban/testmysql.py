import MySQLdb
db_conn = MySQLdb.connect('127.0.0.1', user='root', passwd='1232123', db='test')
db_curs = db_conn.cursor()
db_curs.execute("insert into user values(3,'lannister')")
db_curs.execute("select * from user")
for data in db_curs.fetchall():
    print data
