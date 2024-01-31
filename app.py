import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import json
import datetime
import plotly.express as px
from an_lib import get_all_issues_data,get_total_issues_count
import time
from streamlit_extras.stateful_button import button


# Header
st.header("Turn JQL result into a .CSV (>1000 issues)")

# Introduction
#project%20%3D%20TIMFPT%20and%20issuekey%20<%20TIMFPT-10


    ## Jira Host (type: https://your-domain.atlassian.net)
jira_host = st.text_input(label="Your JIRA Host",value="https://leanprojectmanager.atlassian.net",disabled=False,key="jira_host")

api_url_v3 = f"{jira_host}/rest/api/3"

## JIRA account
jira_account = st.text_input(label="Your JIRA Account",placeholder="Please enter your email",value="anle.projectmanager@gmail.com",key="jira_account")
if "@" not in jira_account:
    st.error("Please input correct email format")
else:
    pass
## API token

jira_api_token = st.text_input(label="Your API Token",help="https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/",type="password",value="ATATT3xFfGF0RmKs-yDsV6Ytu_Wo5mWcgfwnn0S4VhP6VmNByUhOEd_5f49ml4jOs2hYYyWs2ljoN4gYv-qttBXGTgpJq4VJ-63pRoEFlFrC6UJ8E5a9bqA-rQtuzXMIjEqyBPardzUM_u1TAA4Yz33kUMYb3SeW_rDxIZT62LlSVUh_NO5hSt8=55B1EB52",key="jira_api_token")

## Request information
AUTH = HTTPBasicAuth(jira_account,jira_api_token)
HEADERS = {
    "Accept": "application/json"
}
MAX_PAGE_SIZE = 100

# ----------------------------------------------------------------------
st.markdown("---")

# Side bar 
with st.sidebar:
    st.sidebar.title("Menu")
    guideline = st.sidebar.link_button(label="Guideline",url="https://google.com/")


# Export to CSV 
st.header("See Dataframe")

## Jira JQL Filter
jql_filter = st.text_input(label="JQL filter (from URL)",value="project%20%3D%20TIMFPT%20and%20issuekey%20<%20TIMFPT-300",key="jql_filter")

## Show Pandas Dataframe
if 'get_dataframe_button_clicked' not in st.session_state:
        st.session_state.get_dataframe_button_clicked = False
        
def set_get_dataframe_button_cliked():
        st.session_state.get_dataframe_button_clicked = True

            

st.button(label="Get dataframe",type="primary",on_click=set_get_dataframe_button_cliked)

@st.cache_data
def return_df(jql_filter: str,MAX_PAGE_SIZE: int,api_url_v3: str,_AUTH):
    total_issues_count = get_total_issues_count(jql=jql_filter,max_page_size=MAX_PAGE_SIZE,api_url=api_url_v3,authentication_object=AUTH)
    data = get_all_issues_data(jql=jql_filter,api_url=api_url_v3,total_issues_count=total_issues_count,max_page_size=MAX_PAGE_SIZE,authentication_object=AUTH)
    return data

if st.session_state.get_dataframe_button_clicked:       
    # Send a quick request to check response status code
    response = requests.request("GET","https://leanprojectmanager.atlassian.net/rest/api/3/issue/TIMFPT-1",headers=HEADERS,auth=AUTH)
    if jira_account != "" and jira_api_token != "":
        if response.status_code == 200:
            st.success(f"Successfully connected!")
            
            df = return_df(jql_filter= jql_filter,MAX_PAGE_SIZE=MAX_PAGE_SIZE,api_url_v3=api_url_v3,_AUTH=AUTH)
            
            print("done")
            
            st.dataframe(df,hide_index=True)
            
            column_headers = list(df.columns.values)
                        
            def set_columns_selected(*args):
                    print(*args)
                    st.session_state.columns_selected += args
            
            columns_selected = st.sidebar.multiselect(label="Filter your data frame columns",options=column_headers,placeholder="Choose an option",default=column_headers[:2],key="columns_selected",on_change=set_columns_selected)
            
            st.sidebar.write(columns_selected)

            filtered_dataframe = df[columns_selected]
            st.dataframe(filtered_dataframe)

        else:
            st.error(f"Please check your credentials again! Status code: {response.status_code}")
    else:
        st.error("Username and password must not be blank!")
else:
    pass

## Filter the dataframe

## Session State object
st.header("Session State")
st.write(st.session_state)



## Filter the dataframe

with st.sidebar:
    selected = option_menu("Menu",["Home","Filter",default_index=0])