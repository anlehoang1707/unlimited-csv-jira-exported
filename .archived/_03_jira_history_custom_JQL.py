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

JQL = '(Sprint%20%3D%20664%20OR%20labels%20in%20(An_DragonS27))'
JIRA_filter=f'https://storai.atlassian.net/rest/api/3/search?jql={JQL}&maxResults=100&startAt=0'
auth = HTTPBasicAuth("an.l@stor.ai", "ATATT3xFfGF0kDoBFRHam1TLrhKmOYNvUypSqFaFoVpd_aARZy2gFyurVT_8w6dAMbXQffMfa9E0Yq9d-CoMk3Ohkoah22_vW2l7G7DpNmN2rx4TTbXohsshfLKB4dDr9xz2J8Vx0qmaD86C7yn15jpVbOpwrUnVeRABYHCPquYY5U29GkXMev8=835F26FE")
headers = { "Accept": "application/json"}
total_issues = requests.request("GET",JIRA_filter,headers=headers,auth=auth).json()["total"]
print(f'Total issues: {total_issues}')
JIRA_page = 0
remaining_JIRA_page = total_issues%100


issue_list = []
while JIRA_page <= total_issues:
    URL = f'https://storai.atlassian.net/rest/api/3/search?jql={JQL}&maxResults=100&startAt={JIRA_page}'
    #headers = { "Accept": "application/json"}
    response = requests.request("GET",URL,headers=headers,auth=auth)
    print(response.status_code)
    issue_keys = response.json()
    filtered_issues = []
    if ((total_issues-JIRA_page)> remaining_JIRA_page):
        for x in range(1,100):
            items = issue_keys["issues"][x]["key"]
            print (type(items))
            filtered_issues.append(items)
    else:
        for x in range(1,remaining_JIRA_page):
            items = issue_keys["issues"][x]["key"]
            print (type(items))
            filtered_issues.append(items)
    JIRA_page += 100
    issue_list.append(filtered_issues)

issue_list = issue_list[0]

#issue_list = ['ECOM-1890','ECOM-2555','ECOM-1789']
print(issue_list)

appended_data = []
for key in issue_list:
    print("Getting history of:", key,"...")
    auth = HTTPBasicAuth("an.l@stor.ai", "ATATT3xFfGF0kDoBFRHam1TLrhKmOYNvUypSqFaFoVpd_aARZy2gFyurVT_8w6dAMbXQffMfa9E0Yq9d-CoMk3Ohkoah22_vW2l7G7DpNmN2rx4TTbXohsshfLKB4dDr9xz2J8Vx0qmaD86C7yn15jpVbOpwrUnVeRABYHCPquYY5U29GkXMev8=835F26FE")
    URL = f'https://storai.atlassian.net/rest/api/2/issue/{key}/changelog?maxResults=100&startAt=0'
    headers = { "Accept": "application/json"}
    total = requests.request("GET",URL,headers=headers,auth=auth).json()["total"]
    print(total)
    page = 0
    remaining_count = total%100
    while page <= total:
        URL = f'https://storai.atlassian.net/rest/api/2/issue/{key}/changelog?maxResults=100&startAt={page}'
        headers = { "Accept": "application/json"}
        response = requests.request("GET",URL,headers=headers,auth=auth)
        print(response.status_code)
        issue_history = response.json()
        filtered_data = []
        if ((total-page)>remaining_count):
            for x in range(1,100):
                items = issue_history["values"][x]["items"]
                #print (type(items))
                items_string = ''.join(map(str, items))
                #print(type(items_string))
                #print(x)
                df = pd.DataFrame(issue_history["values"][x]["items"])
                createdDate = issue_history["values"][x]["created"]
                id = issue_history["values"][x]["id"]
                df.insert(1,"key",f'{key}')
                df.insert(2,"dateExport",date.today())
                df.insert(3,"historyId",id)
                df.insert(4,"dateCreated",createdDate)
                df.insert(5,"page",page)
                pprint(items)
                pprint(df)
                filtered_data.append(df)
        else:
            if issue_history["values"] != []:
                for x in range(1,remaining_count):
                    items = issue_history["values"][x]["items"]
                    #print (type(items))
                    items_string = ''.join(map(str, items))
                    #print(type(items_string))
                    #print(x)
                    df = pd.DataFrame(issue_history["values"][x]["items"])
                    createdDate = issue_history["values"][x]["created"]
                    id = issue_history["values"][x]["id"]
                    df.insert(1,"key",f'{key}')
                    df.insert(2,"dateExport",date.today())
                    df.insert(3,"historyId",id)
                    df.insert(4,"dateCreated",createdDate)
                    df.insert(5,"page",page)
                    pprint(items)
                    pprint(df)
                    filtered_data.append(df) 
            else:
                print('Nothing was changed')
                #,field,key,dateExport,historyId,dateCreated,page,fieldtype,from,fromString,to,toString
                df = pd.DataFrame(issue_history["values"])
                print(type(df))
                df["key"] = ""
                df["dateExport"] = ""
                df["historyId"] = ""
                df["dateCreated"] = ""
                df["page"] = ""
                df["fieldtype"] = ""
                df["from"] = ""
                df["fromString"] = ""
                df["to"] = ""
                df["toString"] = ""
                df.loc["0","key"] = f'{key}'
                df.loc["0","dateExport"] = date.today()
                filtered_data.append(df)
        page += 100
        filtered_data = pd.concat(filtered_data)
    appended_data.append(filtered_data)

appended_data = pd.concat(appended_data)
pprint(appended_data)
appended_data.to_csv('history_custom_jql.csv')






