*** Settings ***
Library  /Users/abhaybhargav/Documents/Code/Python/RoboBandit/robobandit/RoboBandit.py

*** Variables ***
${CODE_PATH}  /Users/abhaybhargav/Documents/Code/Python/defcon_app/app
${RESULTS_PATH}  /Users/abhaybhargav/Documents/Code/Python/RoboBandit/test

*** Test Cases ***
Run Bandit against Source Code
    run bandit against python source  ${CODE_PATH}  ${RESULTS_PATH}

Run Safety against Requirements File
    run safety against python source  ${CODE_PATH}  ${RESULTS_PATH}
