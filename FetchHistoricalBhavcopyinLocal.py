import requests
from zipfile import ZipFile
import os
import datetime
import calendar
import holidays
import time

# years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
years = [2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
path = "W:/Python/AlgoTradingNSE/NSEHistoricalBhavCopy/DATA/"

def getUrl(ex):
    return "https://archives.nseindia.com/content/historical/EQUITIES/"+ ex


def getDays(y,m):
    return calendar.monthrange(years[y],m+1)[1]

def getStr(val):
    if(val<9):
        return "0"+str(val+1)
    else:
        return str(val+1)

def isWeekday(y,m,i):
    x = datetime.datetime(years[y],m+1,i+1)
    weekd = int(x.strftime("%w"))
    if(weekd != 0 and weekd != 6):
        return True
    return False

def isHoliday(u,m,yearex):
    h = holidays.IND()
    holidaydate = ''+u+'-'+m+'-'+yearex
    if(holidaydate in h):
        return True
    return False

start_time = time.time()
for year in range(len(years)):
    yearex = str(years[year])

    for month in range(len(months)):
        monthex = months[month]
        days = getDays(year,month)
        m = getStr(month)

        for i in range(days):

            if(isWeekday(year,month,i)):
                u = getStr(i)

                if(not(isHoliday(u,m,yearex))):
                    filename = "cm"+u+monthex+yearex+"bhav.csv.zip"
                    extension = yearex+"/"+monthex+"/"+filename
                    url = getUrl(extension)
                    print(url)
                    try:
                        response = requests.get(url,stream=True,timeout=2)
                        if(response.status_code == 200):
                            with open(filename,'wb') as f:
                                f.write(response.content)

                            with ZipFile(filename, 'r') as zip_ref:
                                zip_ref.extractall(path+yearex+"/"+monthex)
                                print("PATH :"+path+yearex+"/"+monthex)

                            os.remove(filename)
                    except Exception as e:
                        print("err")

print("--- %s seconds ---" % (time.time() - start_time))