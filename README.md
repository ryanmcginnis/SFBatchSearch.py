## Overview
SFBatchSearch makes large searches in Salesforce Console simple. The program accepts a plain text file containing a list of search terms and executes the search automatically. 

## Use Case
Salesforce Console does not provide batch search functionality outside of the SOAP API. Often, a large list of terms (such as case numbers, customer email addresses, or knowledge article titles) needs to be queried by users quickly. Users may not have access to the API, or may have no knowledge of how the API works.

SFBatchSearch relies on the basic Python library and your web browser to parse a list of terms and return the results in browser tabs. 

## Compatibility
SFBatchSearch was written for, and tested under, macOS and Linux. Currently, the program may crash on Windows systems at `system('clear')`. If you encounter this problem:

1. Open SFBatchSearch in your editor
2. Change `system('clear')` to `system('CLS')`
3. Save the file

## Workflow
Run `python /path/to/script.py /path/to/file.txt` as illustrated below.

![img1](https://github.com/ryanmcginnis/SFBatchSearch.py/blob/master/images/img1.png)

The program opens the Salesforce login page in your web browser. Because the program does use the Salesforce SOAP API, the user must manually log in. Log in to Salesforce, then return to the program and press the Return key. If you are already logged in, press the Return key.

![img2](https://github.com/ryanmcginnis/SFBatchSearch.py/blob/master/images/img2.png)

The search should begin immediately, and end on its own.

![img3](https://github.com/ryanmcginnis/SFBatchSearch.py/blob/master/images/img3.png)
