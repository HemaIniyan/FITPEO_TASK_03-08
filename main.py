from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep


def update_text_field(new_value):
    sleep(4)
    input_text = driver.find_element(By.XPATH, "//input[@type='number']")
    input_text .click()
    input_text .send_keys(Keys.CONTROL + "a")  # Select all text
    input_text .send_keys(Keys.BACKSPACE)  # Delete selected text
    input_text .send_keys(new_value)  # Enter the new value


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# TASK 1 - Navigate to the FitPeo Homepage:
driver.get("https://www.fitpeo.com/")
sleep(2)


# TASK 2 - Navigate to the Revenue Calculator Page:
driver.find_element(By.XPATH, "//a[@href='/revenue-calculator']").click()


# TASK 3 - Scroll Down to the Slider section:
sleep(5)
driver.execute_script("window.scrollBy(0,450)")


# TASK 4 - Adjust the Slider:
sleep(3)
slider = driver.find_element(By.XPATH, "//input[@type='range']")

# Define the desired point to which you want to drag the slider
desired_position = 820

# Get the initial position of the slider
initial_x = slider.location['x']
slider_width = slider.size['width']
slider_value = desired_position / 175.0  # Adjusted based on slider scale

# Calculate the new position
new_x = initial_x + slider_width * slider_value

# Create ActionChains instance
actions = ActionChains(driver)

# Perform the drag-and-drop action
actions.click_and_hold(slider).move_by_offset(new_x - initial_x, 0).release().perform()
driver.execute_script("window.scrollBy(0,400)")
# Move the slider to the desired position
for i in range(4):
    slider.send_keys(Keys.RIGHT)


# TASK 5 -  Update the Text Field:
update_text_field('560')


# TASK 6 - Validate Slider Value:
input_field = driver.find_element(By.XPATH, "//input[@type='number']")
print(f"Slider value is:{input_field.get_attribute('value')}")


# TASK 7 - Select CPT Codes:
sleep(2)
driver.execute_script("window.scrollBy(0,400)")
checkbox = driver.find_elements(By.XPATH, value="//input[@type='checkbox']")
for i in [0, 1, 2, 7]:
    checkbox[i].click()
    sleep(2)
driver.execute_script("window.scrollBy(0,-1600)")


# TASK 8 - Validate Total Recurring Reimbursement:
update_text_field('820')
sleep(2)
driver.execute_script("window.scrollBy(0,100)")


# TASK 9 - verify the header:
sleep(2)
header=driver.find_element(By.XPATH, "//*[contains(text(), 'Total Recurring Reimbursement for all Patients Per Month:')]")
print(header.text)

sleep(2)
driver.quit()
