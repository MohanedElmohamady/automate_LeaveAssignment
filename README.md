# Practical Automation Task: OrangeHRM Leave Assignment

This repository contains the solution for the practical automation task provided by Western Union. The task involves automating a leave assignment process in the OrangeHRM system using Python and Selenium.

---

## **Task Description**
The objective was to automate specific HR operations on the OrangeHRM platform as outlined in the provided user stories. The solution addresses critical functionalities and implements error handling for potential obstacles during automation.

---

## **Features**
### **Critical User Stories**
1. **Open the OrangeHRM Website**  
   Navigate to the [OrangeHRM demo page](https://opensource-demo.orangehrmlive.com/).

2. **Log In**  
   Automate login using provided credentials (`admin/admin123`).

3. **Navigate to "Assign Leave"**  
   Access the "Assign Leave" functionality from the dashboard.

4. **Fill Leave Details**  
   - Employee Name: Jasmine Morgan (with backup: James Butler).
   - Leave Type: US - Vacation.
   - From Date: 2020-10-19.
   - To Date: 2020-10-23.
   - Handle partial days: None.

5. **Submit and Confirm Leave**  
   Handle confirmation pop-ups or error messages during submission.

6. **Close the Browser**  
   Shut down the browser upon completion.

### **Additional Features; implemented in V2**
1. **Error Handling for Employee Names**  
   If "Jasmine Morgan" is unavailable:
   - Detect "No Records Found."
   - Clear the field and input the backup name, "James Butler."

2. **Leave Balance Check**  
   - Detect insufficient balance messages.
   - Log balance errors for debugging.

3. **Logout Before Closing**  
   Automate the logout process to maintain system security.

---

## **Solution Overview**
### **Structure**
The solution is implemented in Python using the Selenium library. Key automation tasks include:
- Web element interaction.
- Error detection and handling.
- Keyboard navigation for dropdown selection.

### **Key Challenges & Solutions**
1. **Employee Name Unavailability**  
   Added conditional logic to detect if "Jasmine Morgan" is unavailable and fallback to "James Butler."

2. **Auto-Filled Dates**  
   Implemented clearing mechanisms for date fields to prevent concatenation errors.

3. **Insufficient Balance Check**  
   Integrated detection of error messages for insufficient balance and logged these events.

4. **Confirmation Handling**  
   Managed pop-ups and error prompts using Selenium's explicit wait and exception handling.

---

## **How to Run**
### **Prerequisites**
- Python 3.x installed.
- Install dependencies:
  ```bash
  pip install selenium
- Download the appropriate ChromeDriver for your system.
  
### **Execution**
- Run the script:
  ```bash
  Python code.py

### **Expected Outputs**
- Successful leave submission or error logging.
- Browser closes automatically after the process.

---

## **Potential Improvements**
### **Enhanced Logging:**
- Add a more detailed logging framework for tracking execution steps and errors.
- Include timestamps for easier debugging.

### **Multi-Request Handling:**
- Extend the script to handle multiple leave requests in one session.

### **Dynamic Handling:**
- Develop a more robust framework for managing highly dynamic elements.

### **Integrate with CI/CD:**
- Automate the execution of the script as part of a CI/CD pipeline for continuous testing.

---

## **Challenges Faced**
### **Dynamic Element Loading:**
- Elements on the OrangeHRM platform load dynamically, causing potential issues. This was resolved by using Selenium's explicit waits to ensure elements were fully loaded before interacting with them.

### **Field Reset Issues:**
- Auto-filled fields caused issues with concatenated values. These were managed by combining
  ```bash
  .clear()
and multiple BACKSPACE key inputs to ensure fields were entirely cleared before entering new data.

### **Employee Name Validation:**
- The dropdown menu behavior required handling both "No Records Found" and selecting a valid name using keyboard navigation (ARROW_DOWN and ENTER).

### **Leave Balance Validation:**
- Detecting insufficient balance messages was crucial to prevent submitting invalid leave requests. This was achieved by identifying error messages dynamically.


Let me know if you need additional edits or formatting adjustments!


