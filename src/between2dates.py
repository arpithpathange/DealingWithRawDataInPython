from datetime import date
import datetime
from readJson import read


class dataBetween2dates:

    def getdatabet2dates(self):
        dates=[]
        date_format = "YYYY-MM-DD"
        d1 = datetime.date(2017,8,01)
        d2 = datetime.date(2017,9,01)
        cnt = 0
        readJson = read()
        readJson.readRawData()

        for rowdata in readJson.rawdata:
            now = date(*map(int, rowdata[0].split('-')))
            if (now < d2) & (now > d1):
                cnt = cnt+1
                print rowdata

        print "data between the given dates are " + str(cnt)



readdata = dataBetween2dates()
readdata.getdatabet2dates()

