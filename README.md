# Turn JQL result into a .CSV (>1000 issues)

## Use Cases
- Workflow: Jira data -(REST Python code)-> dataframe -(quite easy)-> .csv.

## Purpose
- Help non-coders to export any JQL result (even > 1000 issues) into .CSV
- Why .CSV?
    - Popular and Friendly
    - Easier manipulation (such as import to Excel pivot/Power BI dashboard)

## Problems to Solve
- Budget:
    - Not all small businesses/star-up companies have budget on buying extensive powerful plugins on Marketplace to visualize data directly on Jira.
- Jira Core plugins:
    - Even though Jira has already supported "Export to .csv"/"Export to Excel", the maximum number of records is 1000.
- Jira Rest API:
    - Allows User to retrieve Jira data in JSON format, which is also hard to manipulate for non-coders.
    - However, the response is paginated (max_result=100 per request). Therefore, one Jira request doesn't give the whole expected result. For JQL of 1000 issues and above, we need to create a common solution.