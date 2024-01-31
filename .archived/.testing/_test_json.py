import pandas as pd
import requests
import json
from requests.auth import HTTPBasicAuth

'''JIRA_HOST = "https://leanprojectmanager.atlassian.net"
API_URL_V3 = f'{JIRA_HOST}/rest/api/3'
USER_NAME = "anle.projectmanager@gmail.com"
API_TOKEN = "ATATT3xFfGF0RmKs-yDsV6Ytu_Wo5mWcgfwnn0S4VhP6VmNByUhOEd_5f49ml4jOs2hYYyWs2ljoN4gYv-qttBXGTgpJq4VJ-63pRoEFlFrC6UJ8E5a9bqA-rQtuzXMIjEqyBPardzUM_u1TAA4Yz33kUMYb3SeW_rDxIZT62LlSVUh_NO5hSt8=55B1EB52"
JQL = "project%20%3D%20TIMFPT%20order%20by%20created%20DESC"
AUTH = HTTPBasicAuth(USER_NAME,API_TOKEN)
HEADERS = {"Accept": "application/json"}
URL = f"{API_URL_V3}/search?=jql={JQL}"

def get_total_issues_count(jql: str, max_page_size: int,url: str) -> int:
    total_issues_url = f'{url}/search?jql={jql}&maxResults={max_page_size}&startAt=0'
    total_issues_count = requests.request("GET", total_issues_url, headers=HEADERS, auth=AUTH).json()["total"]
    print (total_issues_count)
    return total_issues_count

get_total_issues_count(jql= JQL, max_page_size= 100, url= API_URL_V3)
'''



import json

file_name = 'sample_response.json'

with open(file_name, 'r', encoding='utf-8') as f:
    try:
        my_data = json.load(f)  # 👈️ parse the JSON with load()

        print("json test successfully")
    except BaseException as e:
        print('The file contains invalid JSON')
        
df = pd.json_normalize(my_data["issues"], max_level=12)
print(df)

'''df.to_csv("test_json.csv")'''


#jira_fields = df.columns.tolist()
#print(jira_fields)