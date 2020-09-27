from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class qcc_loginpage():
    driver = None
    emailTextbox = (By.CSS_SELECTOR, "input[id='email']")
    passwordTextBox = (By.CSS_SELECTOR, "input[id='password']")
    submitButton = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver):
        self.driver = driver


    def loginToAccount(self, username, password):
        mailTextBox = self.driver.find_element(By.CSS_SELECTOR, "input[id='email']")
        mailTextBox.send_keys(username)

        passwordTextBox = self.driver.find_element(By.CSS_SELECTOR, "input[id='password']")
        passwordTextBox.send_keys(password)

        submitButton = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submitButton.click()

        headerNotchElement = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.ID, "headerNotch")))
        return headerNotchElement
        #--- Assert here by checking the login form visibility


    pass