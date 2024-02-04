# 1. Step 1: Create new Project & Install Required Packages/plugins

#  Selenium. Selenium Libraries
#  pytest: Python framework
#  Pytest-html: PyTest HTML Reports.
#  pytestdist : Run Tests Parallel
#  Openpyxl _: Ms Excel Support
#  Allure-pytest: to generate allure reports

# Step 2: Create Folder Structure

# Configuration(Folder)
# pageObject (package)
# testCases (package)
# TestData(Folder)
# Logs(Folder)
# Screenshot(Folder)
# Reports(Folder)
# Run.bat (File)

# 3. Step 3 : Automating Login Test Case

# 1. Create Object Class under "pageObjects"  /////
# 2. Create test cases under "testCases"
# 3. Create conftest.py under "testCases" Project Name

# 4.Step 4 : Capture screenshot on failures

# Capture the screenshots under “Screenshots folder”
# 5. Step 5: Read common values from ini file

# 1. Add "config.ini" file in "Configurations" folder
# 2. Create "readProperties.py" utility file under utilities package
# to read common data.
# 3. Replace hard coded values in test case

# 6. Step 6: Adding logs to test case

# 1. Add Logger.py under utilities package.
# 2. Add logs to test case.

# 7. Step 7: Run Tests on Desired Browser/Cross

# Browser/Parallel
# 1. update contest.py with required Fixtures which will accept
# command line argument (browser)
# 2. Pass browser name as argument in command line
# 3. To Run tests on desired browser
# pytest -s -v testCases/testcasename.py --browser chrome
# Pytest -s -v testCases/testcasename.py --browser firefox
# 4. To Run tests parallel
# pytest -s -v -n=3 testCases/testcasename.py --browser edge
# pytest -s -v -n=3 testCases/testcasename.py --browser
# chrome
# pytest -s -v -n=3 testCases/testcasename.py --browser firefox

# 8. Step 8: Genérate pytest HTML Reports

# 1. Update conftest.py with pytest hooks
# 2. To Generate HTML report run below command:
# pytest -s -v -n=3 --html=Reports\report.html testCases/testcasename.py -“browser chrome”

# 9. Step 9: Automating Data Driven Test Case

# 1. Prepare test data in Excel sheet, place the excel file inside the
# TestData folder.
# 2. Create " XLUtils.py” class under utilities package.
# 3. Create LoginDataDrivenTest under testCases
# 4. Run the test case

# 10. Step 10: Adding new testcases

# 11. Step 11: Grouping Tests

# 1. Grouping markers( Add markers to every test method)
# @pytestmark.sanity
# @pytestmark.regression
# 2. Add Marker entries in pytes.ini file
# Pytestini
# -----------
# [pytest]
# Markers = sanity

# 12. Step 12: Create Run.bat file in project folder

# pytest –n=3 -m "sanity" --html=./Reports/report.html testCases/

# 13. Step 13: Run the Test Cases using jenkins

# 14. Step 14: Push the build in git hub