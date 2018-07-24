import pymysql
import xlrd


#Ack with Database - -handshaking
conn = pymysql.connect(port=3306,host='localhost', user='root', passwd='admin123', db='pythondb')

#Communication channel
cur = conn.cursor()
#cur.execute('create table empinfo (id INT AUTO_INCREMENT PRIMARY KEY,name varchar(20),dept varchar(10),salary int(10))')
#cur.execute('insert into empinfo values(1,\'Thomas1\',\'Sales\',5000)')
#cur.execute('insert into empinfo values(2,\'Thomas2\',\'Sales\',6000)')
#cur.execute('insert into empinfo values(3,\'Thomas3\',\'Sales\',7000)')
#cur.execute('insert into empinfo values(4,\'Thomas4\',\'Sales\',25000)')
cur.execute('select * from empinfo')
print(cur.fetchmany(2))



#conn.commit()

#cur.execute('insert into employee values(200,\'Jason\',\'Technology\',5500)')
#print(cur.description)
#conn.commit()
#cur.execute('select * from employee')
#list = cur.fetchmany(2)

#print(list)
'''
for row in cur:
    print(row)
'''
cur.close()
conn.close()