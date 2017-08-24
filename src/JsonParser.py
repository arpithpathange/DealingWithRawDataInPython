import simplejson as json
from readJson import read


class GetAllData:

    def getAllData(self):
        readJson = read()
        readJson.readRawData()

        for name in readJson.colname:
            print name +"         ",
        else:
            print

        for rowdata in readJson.rawdata:
            for eachcol in rowdata:
                print str(eachcol)+"      ",
            else:
                print


getData = GetAllData()
getData.getAllData()




