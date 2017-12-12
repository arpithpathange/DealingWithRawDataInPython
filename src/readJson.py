import simplejson as json

class read:
    colname = None
    rawData = None


    def readRawData(self):
        with open('data.json') as json_data:
            parserJson = json.load(json_data)
            self.colname = parserJson['column_names']
            self.rawdata = parserJson['data']

