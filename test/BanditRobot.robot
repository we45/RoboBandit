*** Settings ***
Library  /Users/abhaybhargav/Documents/code/python/RoboBandit/robobandit/RoboBandit.py

*** Variables ***
${CODE_PATH}  /Users/abhaybhargav/Documents/code/python/ThreatPlaybook/api
${RESULTS_PATH}  /Users/abhaybhargav/Documents/code/python/RoboBandit/test

*** Test Cases ***
Run Bandit against Source Code
    run bandit against python source  ${CODE_PATH}  ${RESULTS_PATH}

Run Safety against Requirements File
    run safety against python source  ${CODE_PATH}  ${RESULTS_PATH}
