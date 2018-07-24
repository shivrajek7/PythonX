import xlrd as read
import xlwt as write
import os


class ExcelOperations :

    filePath ='E:\pythonworkspace\excelfile\\userInfo.xls'
    listOfLines = []
    readExcelDataList=[]

# This function will read text file and get the lines and put it into list
    # listOfLines  -- which a globle varible in ExcelOperations -- read line append it into list -- strip (removes \n)
    def getDataFromFile(self):
        file = open('E:\pythonworkspace\excelfile\sampl.txt')
        for line in file.readlines():
            ExcelOperations.listOfLines.append(line.strip())

    def writeIntoExcel(self):
        workBook = write.Workbook()
        userInfoSheet = workBook.add_sheet('UserInfo')
        count = 0
        cols = []
        for item in ExcelOperations.listOfLines:
            for words in item.split(','):
                cols.append(words)

        for num in range(ExcelOperations.listOfLines.__len__()):
            row = userInfoSheet.row(num)
            for item in range(3):
                row.write(item,cols.__getitem__(count))
                count+=1

        workBook.save(ExcelOperations.filePath)


    def readDataFromExcel(self):
        workbook = read.open_workbook(ExcelOperations.filePath)
        userinfosheet = workbook.sheet_by_name("UserInfo")

        for rindex in range(0,userinfosheet.nrows):
            for cindex in range(0,userinfosheet.ncols):
                ExcelOperations.readExcelDataList.append(userinfosheet.cell(rindex,cindex).value)
        print(ExcelOperations.readExcelDataList)
        return ExcelOperations.readExcelDataList



if __name__ == '__main__':
    ob = ExcelOperations()
    print('get data from File to Python')
    ob.getDataFromFile()
    print(ExcelOperations.listOfLines)
    print('file--python data to Excel')
    ob.writeIntoExcel()
    print('excel to python')
    ob.readDataFromExcel()
