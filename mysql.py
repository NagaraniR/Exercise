import MySQLdb
db=MySQLdb.connect(host='localhost',user='root',passwd="root",db="nagarani")
cur=db.cursor()
cur.execute("SELECT * FROM empOne")
for row in cur.fetchall():
    print row[0],"",row[1]
