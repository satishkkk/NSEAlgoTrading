from NSEHistoricalBhavCopy.util import dbconnectionutils
import pandas as pd
from datetime import datetime
def fetchdata(connection):
    connection = dbconnectionutils.getConnection()
    print("Connected . . . ")
    sql = " select * from bhavcopy"
    try:
        cursor =connection.cursor()
        cursor.execute(sql)
        print ( "cursor desc :",cursor.description)
        for row in cursor:
            print(" ----------- ")
            print("Row: ", row)
    finally:
        connection.close()

def insert(df):
    # sql = "Insert into Salary_Grade (Grade, High_Salary, Low_Salary) " \
    #      + " values (%s, %s, %s) "

    connection = dbconnectionutils.getConnection()
    print("Connected . . . ")

    sql = "INSERT INTO `algotreading`.`bhavcopy`(`symbol`,`open`,`high`,`low`,`close`,`last`,`previous_close`,`total_traded_quantity`,`total_traded_value`,`date`,`active_status`,`created_date`,`updated_Date`,`is_delete`)"\
            +"VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s,%s)"

    for row in df.itertuples():
        try:
            cursor =connection.cursor()
            date_time_obj = datetime.strptime(row[11], '%d-%b-%Y')
            # output :  '2000-12-20 10:01:00' YYYY-mm-dd hh:mm:ss
            formatted_date = date_time_obj.strftime('%Y-%m-%d %H:%M:%S')
            insertedDate= datetime.now()
            cursor.execute(sql,(row[1],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],formatted_date, '1', insertedDate, insertedDate,'0'))
            connection.commit()
        except SystemError:
            print("ERROR:")

    connection.close()

def insertdf():
    df = pd.read_csv("W:/Python/AlgoTradingNSE/NSEHistoricalBhavCopy/DATA/2020/JAN/cm01JAN2020bhav.csv", header=[1, 2])
    print(df)


if __name__ == '__main__':
    #fetching data from db
    # fetchdata()

    # insert data into db
    # insert()
    insert(df)