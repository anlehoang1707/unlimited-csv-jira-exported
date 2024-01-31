import requests
import json
import pandas as pd
from pandas import json_normalize
from datetime import datetime, timedelta, date
from requests.auth import HTTPBasicAuth
from pprint import pprint
from An_lib import get_all_issues_data,get_total_issues_count


USER_NAME = "anle.projectmanager@gmail.com"
API_TOKEN = "ATATT3xFfGF0RmKs-yDsV6Ytu_Wo5mWcgfwnn0S4VhP6VmNByUhOEd_5f49ml4jOs2hYYyWs2ljoN4gYv-qttBXGTgpJq4VJ-63pRoEFlFrC6UJ8E5a9bqA-rQtuzXMIjEqyBPardzUM_u1TAA4Yz33kUMYb3SeW_rDxIZT62LlSVUh_NO5hSt8=55B1EB52"
AUTH = HTTPBasicAuth(USER_NAME,API_TOKEN)
JQL = "order%20by%20created%20DESC"
JIRA_HOST = "https://leanprojectmanager.atlassian.net"
API_URL_V3 = f'{JIRA_HOST}/rest/api/3'
HEADERS = {"Accept": "application/json"}
MAX_PAGE_SIZE = 100

total_issues_count = get_total_issues_count(jql=JQL,max_page_size=MAX_PAGE_SIZE,api_url=API_URL_V3)

result = get_all_issues_data(jql=JQL,api_url=API_URL_V3,total_issues_count=total_issues_count,max_page_size=MAX_PAGE_SIZE)

