from ExcelOperations import ExcelOperations
import pymysql
import time

class DbOperations :

    #def __init__(self):
       #print('--',ExcelOperations().readDataFromExcel())

    def createDataBaseTable(self):
        connection = self.getConnection()
        cur = connection.cursor()
        cur.execute('create table user_credentails (id INT AUTO_INCREMENT PRIMARY KEY,username varchar(100),password varchar(100),expectedmsg varchar(100))')
        connection.commit()
        print('\n\nUser_Credentials Table created successfully...with ID/UserName/Password/ExpMsg')
        time.sleep(2)


    def insertIntoDatabase(self,list):
        #self.createDataBaseTable() -- first time required to call this
        connection = self.getConnection()
        cur = connection.cursor()
        cnt = 0
        print('No of Cells --',list.__len__())
        noOfRecords = list.__len__()/3;
        for sno in range(1,int(noOfRecords+1)):
            print(cnt)
            sql_query = 'insert into user_credentails(username,password,expectedmsg) values(''\''+list[cnt]+'\''+',\''+list[cnt+1]+'\','+'\''+list[cnt+2]+'\')'
            print('\n'+sql_query)
            cnt+=3
            cur.execute(sql_query)
            connection.commit()
            time.sleep(5)
        print('\n\n All Records inserted into DB')


    def getConnection(self):
        conn = pymysql.connect(port=3306, host='localhost', user='root', passwd='admin123', db='pythondb')
        #print('\n Inside getconnection ',conn)
        return conn

    def dropTable(self):
        connection = self.getConnection() #Ack
        cur = connection.cursor() # Communication Channel
        cur.execute('drop table user_credentails')
        connection.commit()
        print('\n Table deleted Successfully....!')

    def getAllRecordsFromDbIntoList(self):
        listOfRecordsFrmDb = []
        connection = self.getConnection()
        cur = connection.cursor()
        cur.execute('select * from user_credentails')
        rows=cur.fetchall()
        #print('Rows From DB',rows)
        for items in rows:
            print(items)
            listOfRecordsFrmDb.append(items)
        print(listOfRecordsFrmDb)
        return listOfRecordsFrmDb



    def writeDataIntoFile(self,list):
        file = open('E:\pythonworkspace\excelfile\\dbtofile.txt','w')
        for tpl in list:
            line=''
            for item in tpl:
                line += str(item)+','

            print(line[:-1])
            file.write(line[:-1] +'\n')
        file.close()

    def readDataFromFile(self):
        file = open('E:\pythonworkspace\excelfile\\dbtofile.txt', 'w')
        for lines in file.readlines():
            print(lines)


if __name__ == '__main__':
    ob = ExcelOperations()
    print('get data from File to Python')
    ob.getDataFromFile()
    print(ExcelOperations.listOfLines)
    print('file--python data to Excel')
    ob.writeIntoExcel()
    print('excel to python')
    excelToPythonList = ob.readDataFromExcel()

    print('database stuff')
    dbOb = DbOperations()
    dbOb.dropTable()
    print('table dropped..waiting for 2 seconds')
    time.sleep(2)

    dbOb.createDataBaseTable()
    print('Table Created..waiting for 2 seconds')
    time.sleep(10)
    dbOb.insertIntoDatabase(excelToPythonList)
    dbToFileList = dbOb.getAllRecordsFromDbIntoList()
    dbOb.writeDataIntoFile(dbToFileList)

