from jiraone import LOGIN, PROJECT, file_reader
from jiraone.module import time_in_status
import json

config = json.load(open('../config.json'))
LOGIN(**config)
key = {"jql": "issuetype in (Sub-task,Bug) AND (Sprint = 664 OR labels in (An_DragonS27))"}

#Reference: https://community.atlassian.com/t5/Jira-articles/Getting-time-in-status-using-API/ba-p/1814555

if __name__ == "__main__":     
    time_in_status(PROJECT, key, file_reader, pprint=True, is_printable=False,     
    output_format="json", report_folder="STATUSPAGE", report_file="time1.csv", login=LOGIN, output_filename="result")