#!/usr/bin/env python3

import json

with open('/workspace/json-practice/data/schacon.repos.json', 'r') as file:
    data = json.load(file)
    

for d in data[0:5]:
   name1 = (d['name'])
   html1 = (d['html_url'])
   updated1 = (d['updated_at'])
   visi1 = (d['visibility'])
   records1 = (name1 + ", " + html1 + ", " + updated1 + ", " + visi1+ " \n")
   file1 = open('/workspace/json-practice/lab 8/chacon.csv', 'a')
   file1.write(records1)
    


   