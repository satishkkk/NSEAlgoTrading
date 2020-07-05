import pandas
from datetime import datetime
def main():
   print("hello")
   date= '01-JAN-2020'
   date_time_obj = datetime.strptime(date, '%d-%b-%Y')
   # output :  '2000-12-20 10:01:00' YYYY-mm-dd hh:mm:ss
   formatted_date = date_time_obj.strftime('%Y-%m-%d %H:%M:%S')
   print(formatted_date)
   insertedDate = datetime.now()
   print(insertedDate)
if __name__ == '__main__':
    main()