__author__ = 'arpith.pathange'

from datetime import date
import datetime
from readJson import read
import matplotlib.pyplot as plt


class monthlytopandlow:

    readJson = read()
    monthlist = []
    monthhighdata = []
    monthlowdata = []




    def getdatabet2dates(self,year):
        dates=[]
        date_format = "YYYY-MM-DD"
        self.readJson.readRawData()
        print "Max "+ "min "+ "Month "
        for i in range(1,12):
            #d1 = '2016,'+str(i)+',01'
            #year = 2016
            day = 01
            j = i+1
            d1 = datetime.date(int(year),int(i),int(day))
            d2 = datetime.date(int(year),int(j),int(day))
            self.getdataforamonth(d1, d2)
            print max(self.monthhighdata), min(self.monthlowdata), i
            self.monthlowdata = []
            self.monthhighdata = []






    def getdataforamonth(self, d1, d2):
         for rowdata in self.readJson.rawdata:
            now = date(*map(int, rowdata[0].split('-')))
            if (now < d2) & (now > d1):
                self.monthhighdata.append(rowdata[2])
                self.monthlowdata.append(rowdata[3])






year = 2016
readdata = monthlytopandlow()
avglist = []
yearlist = []
readdata.getdatabet2dates(year)





