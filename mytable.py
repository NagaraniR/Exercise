import MySQLdb
 
db = MySQLdb.connect(host="localhost",  
                     user="root",       
                     passwd="root",    
                     db="test")   
cur = db.cursor()
cur.execute("SELECT * FROM examples")     
for row in cur.fetchall() :
    print row[0], " ", row[1]
