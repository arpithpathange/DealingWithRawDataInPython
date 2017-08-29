import simplejson as json
from readJson import read

class changemeanbetRange:

    def getrange(self):
        reqdata =[]
        readJson = read()
        readJson.readRawData()
        for rowdata in readJson.rawdata:
            if rowdata[5] > 1:
                reqdata.append(rowdata[5])

        print sum(reqdata)/len(reqdata)

range = changemeanbetRange()
range.getrange()