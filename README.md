# SFBatchSearch.py

## Overview
BatchSearch.py makes batch searching in Salesforce Console simple. The script accepts a plaintext file containing a list of search terms and executes the search automatically. 

## Use Case
Salesforce Console does not provide batch search functionality outside of the API. Often, a large list of terms (case numbers, customer email addresses, article titles) needs to be queried by users quickly.

BatchSearch.py relies on the basic Python library and your web browser to parse a list of terms and return the results in browser tabs. 

## Compatibility
BatchSearch.py was written and tested for macOS and Linux. Currently, the script may crash on Windows systems at `system('clear')`. If you encounter this problem:

1. Open the BatchSearch.py in a text editor.
2. Change `system('clear')` to `system('CLS')`
3. Save the file.

## Workflow
1. Run python /path/to/script/ /path/to/file.txt as illustrated below.

2. The program opens the Salesforce login page in your web browser. Because the program does not rely on the Salesforce API, the user must manually log in. Log in to Salesforce, then return to the CLI and press the Return key. If you are already logged in, press the Return key.

3. The search should begin immediately, and end on its own.

