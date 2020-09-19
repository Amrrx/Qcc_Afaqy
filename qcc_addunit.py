# <editor-fold desc="Imports"
import unittest
from faker import Factory
from selenium import webdriver
from qcc_sidemenu import qcc_sidemenu
from qcc_loginpage import qcc_loginpage
from pyunitreport import HTMLTestRunner
from qcc_unitsmodel import qcc_unitsmodel
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# </editor-fold>

# <editor-fold desc="So Variables"
current_URL = "http://stageavl.afaqy.sa/"
chromePath = (r"Z:\AfaqyAutomationPython\chromedriver.exe")
dataGenerator = Factory.create()
global loginPageObject, sideMenuPageObject, unitModelPageObject
# </editor-fold>

class TestAddingUnit(unittest.TestCase):
    # - Step 1 - Start Driver
    def test_start(self):
        driver = webdriver.Chrome(executable_path=chromePath)
        loginPageObject =  qcc_loginpage(driver)
        sideMenuPageObject = qcc_sidemenu(driver)
        unitModelPageObject = qcc_unitsmodel(driver, dataGenerator)
        driver.get(current_URL)
        loginForm = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "form-validation")))
        self.assertIsNotNone(loginForm)

        # - Step 2 - Login to account
        verifyLoginDone = loginPageObject.loginToAccount()
        self.assertIsNotNone(verifyLoginDone)

        # - Step 3 - Navigate to units module
        verifyCurrentPage = sideMenuPageObject.openUnitsModule()
        self.assertIn("- Units", verifyCurrentPage)

        # - Step 4 - Click on Add new unit
        addUnitDialogTitle = unitModelPageObject.openAddUnitDialog()
        self.assertEqual(addUnitDialogTitle, "Add")

        unitModelPageObject.mainTabProcess()

        unitModelPageObject.profileTabProcess()

        unitModelPageObject.groupTabProcess()

        unitModelPageObject.fuelTabProcess()

        unitModelPageObject.sensorTabProcess()

        unitModelPageObject.commandsTabProcess()

        sucessNotification = unitModelPageObject.submitAddingUnit()
        self.assertIsNotNone(sucessNotification)


if __name__ == '__main__':
   unittest.main(testRunner=HTMLTestRunner(output="Reports"))
