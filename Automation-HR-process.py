from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up driver
driver = webdriver.Chrome()  # Ensure path to chromedriver is set
driver.get("https://opensource-demo.orangehrmlive.com/")

# Login
username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
password = driver.find_element(By.NAME, "password")
username.send_keys("admin")  # replace with different credentials if any
password.send_keys("admin123")  # replace with different credentials if any

# Click the login button
driver.find_element(By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]").click()

# Navigate to "Assign Leave" using the title attribute
assign_leave_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@title='Assign Leave']"))
)
assign_leave_button.click()

# Fill Leave Details
# Enter Employee Name
employee_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']")))
employee_name.send_keys("James  Butler")
time.sleep(1)  # Wait for dropdown suggestions to load
employee_name.send_keys(Keys.ARROW_DOWN)  # Navigate to the suggested name
employee_name.send_keys(Keys.ENTER)  # Select the employee name

# Select Leave Type
leave_type_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='oxd-select-text-input']"))
)
leave_type_dropdown.click()

# Select "US - Vacation" from the dropdown options
us_vacation_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='US - Vacation']"))
)
us_vacation_option.click()

# Enter "From Date" and "To Date"
# Locate date fields using the placeholder attribute "yyyy-dd-mm"
from_date = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='yyyy-dd-mm']"))
)
from_date.clear()  # Clear any existing data in the "From Date" field
from_date.send_keys("2020-19-10")  # Enter date in yyyy-dd-mm format

# Locate the "To Date" field
to_date = driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")[1]
to_date.clear()  # Clear any existing data in the "To Date" field
time.sleep(0.5)  # Small pause to allow auto-fill to complete

# Send multiple backspaces to ensure it's empty
for _ in range(10):
    to_date.send_keys(Keys.BACKSPACE)

# Enter the "To Date" value
to_date.send_keys("2020-23-10")  # Enter date in yyyy-dd-mm format

# Submit the form by clicking the "Assign" button
assign_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'oxd-button--secondary')]"))
)
assign_button.click()

# Confirm submission by clicking "OK" if an alert is present
try:
    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@class, 'oxd-button--secondary') and text()=' Ok ']"))
    )
    ok_button.click()
except:
    print("No confirmation alert appeared")

# Log out in two steps
# Step 1: Click on the profile dropdown
profile_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'oxd-userdropdown-tab')]"))
)
profile_dropdown.click()

# Step 2: Click on the "Logout" link from the dropdown
logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/auth/logout' and contains(@class, 'oxd-userdropdown-link')]"))
)
logout_button.click()

# Close browser
driver.quit()
