# Selenium with Python pytest Hybrid Module Framework

This framework is designed to automate web testing using Selenium WebDriver with Python and pytest. It incorporates a hybrid module approach, combining the benefits of both page object model (POM) and module-based organization. Additionally, it implements Data-Driven Testing (DDT) for efficient testing with multiple datasets.

## Features

Project Structure
-Configurations
    -config.ini -contains all prerequisite data
-allureReports
    -contains json file for each test cases
-Reports
    -contains html report of execution
-pageObjects
    - Includes page objects representing web pages with locators and methods.
-testsCases
    -Contains test modules organized by functionality.
-utilities
    -generic selenium functions and utilities file

## Getting Started
1. **Prerequisites:**
   - Python installed on your system.
   - Required Python packages installed. You can install them using pip:

     ```bash
     pip install -r requirements.txt
     ```
#To run the test
    pytest -v -s test_filename.py
    ex. pytest -v -s testCases\test_ProductE2EFlow.py

#Reports
To run tests and generate HTML reports:
    pytest -v -s test_filename.py --html=reports/report.html
    ex. pytest -v -s --html=./Reports/TestE2E.html  testCases\test_ProductE2EFlow.py 
    HTML report: Open Reports/TestE2E.html in a web browser

To run tests and generate Allure reports:
    pytest -v s test_filename.py --alluredir=reports/allure_reports
    ex.pytest -v -s testCases\test_ProductE2EFlow.py --alluredir=allureReports/TestE2E
    Allure report: Run Allure server and open the generated report:
    allure serve allureReports/TestE2E
