import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from pandas import json_normalize
from datetime import datetime,timedelta,date
import numpy as np
from requests.auth import HTTPBasicAuth
from pprint import pprint

payload = { 
	'email': 'an.l@stor.ai', 
	'password': "ATATT3xFfGF0kDoBFRHam1TLrhKmOYNvUypSqFaFoVpd_aARZy2gFyurVT_8w6dAMbXQffMfa9E0Yq9d-CoMk3Ohkoah22_vW2l7G7DpNmN2rx4TTbXohsshfLKB4dDr9xz2J8Vx0qmaD86C7yn15jpVbOpwrUnVeRABYHCPquYY5U29GkXMev8=835F26FE"
}



issue_list = ['ECOM-5319']

appended_data = []
for key in issue_list:
    print("Get history of:", key)
    auth = HTTPBasicAuth("an.l@stor.ai", "ATATT3xFfGF0kDoBFRHam1TLrhKmOYNvUypSqFaFoVpd_aARZy2gFyurVT_8w6dAMbXQffMfa9E0Yq9d-CoMk3Ohkoah22_vW2l7G7DpNmN2rx4TTbXohsshfLKB4dDr9xz2J8Vx0qmaD86C7yn15jpVbOpwrUnVeRABYHCPquYY5U29GkXMev8=835F26FE")
    URL = f'https://storai.atlassian.net/rest/api/2/issue/{key}/changelog'
    headers = { "Accept": "application/json"}
    response = requests.request("GET",URL,headers=headers,auth=auth)
    issue_history = response.json()
    total = issue_history["total"]
    print(response.status_code)
    print(total)
    filtered_data = []
    for x in range(1,total):
        items = issue_history["values"][x]["items"]
        print (type(items))
        items_string = ''.join(map(str, items))
        #print(type(items_string))
        #print(x)
        if "'fieldId': 'status'" in items_string:
            df = pd.DataFrame(issue_history["values"][x]["items"])
            createdDate = issue_history["values"][x]["created"]
            id = issue_history["values"][x]["id"]
            df.insert(1,"key",f'{key}')
            df.insert(2,"dateExport",date.today())
            df.insert(3,"historyId",id)
            df.insert(4,"dateCreated",createdDate)
            pprint(items)
            pprint(df)
            filtered_data.append(df)
        else:
            print("Not status field change")
    filtered_data = pd.concat(filtered_data)
    appended_data.append(filtered_data)

appended_data = pd.concat(appended_data)
pprint(appended_data)
appended_data.to_csv('apphistoryv1.csv')









