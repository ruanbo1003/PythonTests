
import MySQLdb

db = MySQLdb.connect(
    host="192.168.1.121",
    port=3306,
    user="root",
    passwd="root",
    database="irm"
)

db.autocommit(True)

cursor = db.cursor()

cursor.close()
db.close()
