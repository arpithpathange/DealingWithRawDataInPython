import pandas as pd


with open("data.json") as f:
    content = f.read()

dataset = pd.read_json(content, typ='series')
print "Series\n", dataset['column_names']
print "Series\n", dataset['data'][0][0]

