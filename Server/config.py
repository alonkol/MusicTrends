import mysql.connector

# Local
#host = "localhost"
#dbhost = "localhost"
#user = "root"
#password = "DbMysql07"
#dbname = "DbMysql07"

# Production
host = "delta-tomcat-vm"
dbhost = "mysqlsrv.cs.tau.ac.il"
user = "DbMysql07"
password = "DbMysql07"
dbname = "DbMysql07"


dbconnection = mysql.connector.connect(user=user, password=password,
                              host=dbhost,
                              database=dbname)

cursor = dbconnection.cursor(prepared=True)
unsafe_cursor = dbconnection.cursor(dictionary=True)

port = 40335


