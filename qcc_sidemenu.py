from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class qcc_sidemenu:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    # - Step 3 - Units Side Menu
    def openUnitsModule(self):
        sideMenu = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='headerNotch']" + '>' + "button[type='button']")))
        sideMenu.click()

        sideMenuScope = self.driver.find_element(By.TAG_NAME, "afaqy-menu")
        unitsPage = WebDriverWait(sideMenuScope, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href^='/units']")))
        unitsPage.click()

        return self.driver.title
        # --- Assert here by checking the web page title