import csv
from datetime import date
from pprint import pprint
import pandas as pd
import requests
from pandas.core.interchange import dataframe
from requests.auth import HTTPBasicAuth


USER_NAME = "anle.projectmanager@gmail.com"
API_TOKEN = "ATATT3xFfGF0RmKs-yDsV6Ytu_Wo5mWcgfwnn0S4VhP6VmNByUhOEd_5f49ml4jOs2hYYyWs2ljoN4gYv-qttBXGTgpJq4VJ-63pRoEFlFrC6UJ8E5a9bqA-rQtuzXMIjEqyBPardzUM_u1TAA4Yz33kUMYb3SeW_rDxIZT62LlSVUh_NO5hSt8=55B1EB52"
AUTH = HTTPBasicAuth(USER_NAME,API_TOKEN)
HEADERS = {"Accept": "application/json"}

#JQL = "project%20%3D%20TIMFPT%20order%20by%20created%20DESC"

def get_total_issues_count(jql: str, max_page_size: int,api_url: str) -> int:
    total_issues_url = f'{api_url}/search?jql={jql}&maxResults={max_page_size}&startAt=0'
    total_issues_count = requests.request("GET", total_issues_url, headers=HEADERS, auth=AUTH).json()["total"]
    print(total_issues_count)
    return total_issues_count
    # total_issues_count = 3420

'''def get_all_issues_data(jql: str, api_url: str, total_issues_count: int, max_page_size: int) -> dataframe:
    current_index = 0
    issue_count_on_last_page = total_issues_count % max_page_size
    page_count = total_issues_count // max_page_size
    print("Number of page (quotient + 1) is:", page_count+1)
    print("Issue count on last page is:",issue_count_on_last_page)
    all_issues_data = []
    while current_index <= total_issues_count:
        new_url = f'{api_url}/search?jql={jql}&maxResults={max_page_size}&startAt={current_index}'
        response = requests.request("GET", new_url, headers=HEADERS, auth=AUTH)
        print(response.status_code)
        data = response.json()
        
        issues_data_per_page = []
        if ((total_issues_count - current_index) > issue_count_on_last_page):
            for x in range(0, max_page_size):
                issue_data = data["issues"][x]["fields"]
                issues_data_per_page.append(issue_data)
        else:
            for x in range(0, issue_count_on_last_page):
                issue_data = data["issues"][x]["fields"]
                issues_data_per_page.append(issue_data)
        current_index += max_page_size
        all_issues_data += issues_data_per_page
    print("success")
    pprint(type(all_issues_data))
    df = pd.DataFrame(all_issues_data)
    pprint(df)
    df.to_csv("testing_custom.csv")'''

def get_all_issues_data(jql: str, api_url: str, total_issues_count: int, max_page_size: int) -> dataframe:
    current_index = 0
    issue_count_on_last_page = total_issues_count % max_page_size
    page_count = total_issues_count // max_page_size
    print("Number of page (quotient + 1) is:", page_count+1)
    print("Issue count on last page is:",issue_count_on_last_page)
    all_issues_data = []
    while current_index <= total_issues_count:
        new_url = f'{api_url}/search?jql={jql}&maxResults={max_page_size}&startAt={current_index}'
        response = requests.request("GET", new_url, headers=HEADERS, auth=AUTH)
        print(response.status_code)
        data = response.json()
        
        data_array = []
        if ((total_issues_count - current_index) > issue_count_on_last_page):
            for x in range(0, max_page_size):
                df = pd.json_normalize(data["issues"][x],max_level=50)
                data_array.append(df)
        else:
            for x in range(0, issue_count_on_last_page):
                df = pd.json_normalize(data["issues"][x],max_level=50)
                data_array.append(df)
        current_index += max_page_size
        all_issues_data += data_array
    print("successfully")
    df = pd.concat(all_issues_data)
    pprint(df)
    df.to_csv("test_custom_123.csv")

