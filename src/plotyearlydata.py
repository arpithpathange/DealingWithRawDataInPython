__author__ = 'arpith.pathange'

from datetime import date
import datetime
from readJson import read
import matplotlib.pyplot as plt


class plotyearlydata:

    readJson = read()
    monthlist =[]
    monthdata = 0




    def getdatabet2dates(self,year):
        dates=[]
        date_format = "YYYY-MM-DD"
        self.readJson.readRawData()

        for i in range(1,12):
            d1 = '2016,'+str(i)+',01'
            #year = 2016
            day = 01
            d1 = datetime.date(int(year),int(i),int(day))
            d2 = datetime.date(int(year),int(i+1),int(day))
            self.getdataforamonth(d1, d2)



    def getdataforamonth(self, d1, d2):
         for rowdata in self.readJson.rawdata:
            now = date(*map(int, rowdata[0].split('-')))
            if (now < d2) & (now > d1):
                self.monthdata = self.monthdata+rowdata[4]
         self.monthlist.append(self.monthdata)
         self.monthdata =0





readdata = plotyearlydata()
avglist = []
yearlist = []
for x in range(1983, 2016):
    readdata.getdatabet2dates(x)
    #avg = float(sum(readdata.getdatabet2dates ))/len(readdata.getdatabet2dates )
    #print sum(readdata.getdatabet2dates )
    avglist.append(sum(plotyearlydata.monthlist)/ len(plotyearlydata.monthlist))
    yearlist.append(x)

print yearlist
print avglist
#x = [1,2,3,4,5,6,7,8,9,10,11]
plt.plot(yearlist, avglist)
plt.xlabel('Cost')
# naming the y axis
plt.ylabel('Year')

# giving a title to my graph


# function to show the plot
plt.show()


