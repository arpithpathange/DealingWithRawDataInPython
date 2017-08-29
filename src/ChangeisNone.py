import simplejson as json
from readJson import read

class ChangeisNone:
    def checkfornonechange(self):
        reqdata =[]
        readJson = read()
        readJson.readRawData()
        cnt = 0;
        for rowdata in readJson.rawdata:
            if rowdata[5] == None:
                cnt = cnt+1

        print "Count of Change with none value is " + str(cnt)


nonecnt = ChangeisNone()
nonecnt.checkfornonechange()
