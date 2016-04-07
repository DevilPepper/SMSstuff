# This is written for PYTHON 3
# Don't forget to install requests package

import requests
import json



customerId = '56c66be6a73e4927415075d8'
apiKey = '9c4f89803b1ff303f2d50304ba87ebe1'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
status = False
response = requests.get(url)
name = "Prissy"
data = json.loads(response.text)   
for x in range(0, 3):
    if data[x]['first_name'] == name:
        print("Hello Principal")
        status = True

if status == False:
    print("YOU DONT EXIST HERE GET OUT")

