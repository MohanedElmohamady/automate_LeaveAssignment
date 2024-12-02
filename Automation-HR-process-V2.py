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
username.send_keys("admin")  # replace with actual credentials
password.send_keys("admin123")  # replace with actual credentials

# Click the login button
driver.find_element(By.XPATH, "//button[contains(@class, 'orangehrm-login-button')]").click()

# Navigate to "Assign Leave"
assign_leave_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@title='Assign Leave']"))
)
assign_leave_button.click()

# Fill Employee Name with a primary and backup option
def enter_employee_name(name):
    employee_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
    )
    employee_name_field.clear()
    employee_name_field.send_keys(name)
    time.sleep(1)  # Wait for the dropdown to populate

# Try to enter "Jasmine Morgan" first
enter_employee_name("Jasmine Morgan")

# Check for "No Records Found" in dropdown
try:
    no_records = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']//div[@role='option' and text()='No Records Found']"))
    )
    if no_records:
        # Log the issue
        print("Jasmine Morgan not found. Using alternate name.")
        
        # Clear the field and try "James Butler" instead
        employee_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))
        )
        employee_name_field.clear()  # Clear any existing input
        for _ in range(20):  # Send multiple BACKSPACE keys to ensure it's completely cleared
            employee_name_field.send_keys(Keys.BACKSPACE)
        
        # Enter and select the backup name using keyboard navigation
        employee_name_field.send_keys("James Butler")
        time.sleep(1)  # Wait for dropdown to populate with the backup name
        employee_name_field.send_keys(Keys.ARROW_DOWN)  # Navigate to the suggested name
        employee_name_field.send_keys(Keys.ENTER)  # Select the employee name

except:
    # If Jasmine Morgan is available, select it from the dropdown
    jasmine_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']//div[@role='option']//span[text()='Jasmine Morgan']"))
    )
    jasmine_option.click()

# Continue with remaining form fields (example: Leave Type, Dates)

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
from_date = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='yyyy-dd-mm']"))
)
from_date.clear()
from_date.send_keys("2020-19-10")

to_date = driver.find_elements(By.XPATH, "//input[@placeholder='yyyy-dd-mm']")[1]
to_date.clear()
time.sleep(0.5)
for _ in range(10):
    to_date.send_keys(Keys.BACKSPACE)
to_date.send_keys("2020-23-10")

try:
    balance_error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'orangehrm-leave-balance-text') and contains(@class, '--error')]"))
 )
    if balance_error:
        print("Jasmine Morgan has not sufficient balance")

except:
    print("Jasmine Morgan has sufficient balance")
        

# Submit the form
assign_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(@class, 'oxd-button--secondary')]"))
)
assign_button.click()

# Confirm subm
