from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class qcc_unitsmodel:
    driver = None
    dataGenerator = None
    global addUnitDialogUIElement

    def __init__(self, driver, dataGenerator):
        self.driver = driver
        self.dataGenerator = dataGenerator

    def openAddUnitDialog(self):
        pageHeader = self.driver.find_element(By.CSS_SELECTOR, "div[id='page-headers']")
        addUnitButton = pageHeader.find_element(By.CSS_SELECTOR, "a[href='/units/add']")
        addUnitButton.click()
        global addUnitDialogUIElement
        addUnitDialogUIElement = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.TAG_NAME, "afaqy-modal")))
        dialogTitle = addUnitDialogUIElement.find_element(By.TAG_NAME, "h5").get_attribute("innerText")
        return dialogTitle
        # --- Assert here by checking the dialog title = (Add)


    # - Step 5 - Main Tab
    def mainTabProcess(self, devicesList):
        unitNameTextBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "input[testid='name']")
        unitNameTextBox.send_keys(self.dataGenerator.name())

        deviceIMEITextBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "input[testid='imei']")
        deviceIMEITextBox.send_keys(self.dataGenerator.credit_card_number())

        deviceSerialTextBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "input[testid='device_serial']")
        deviceSerialTextBox.send_keys(self.dataGenerator.credit_card_number())

        deviceSIMTextBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "input[testid='sim_number']")
        deviceSIMTextBox.send_keys(self.dataGenerator.credit_card_number())

        simSerialTextBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "input[testid='sim_serial']")
        simSerialTextBox.send_keys(self.dataGenerator.credit_card_number())

        untiDeviceDropBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "select[testid='device']")
        untiDeviceDropBox.click()
        deviceValue = untiDeviceDropBox.find_element(By.CSS_SELECTOR, f"option[value='{self.dataGenerator.random.choice(devicesList)}']")
        deviceValue.click()
        # --- No Assert here

    # - Step 6 - Profile Tab : Tab index = 2
    def profileTabProcess(self):
        self.switchTab(addUnitDialogUIElement, 2)
        # ======================
        unitPlateTextBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "input[testid='plate_number']")
        unitPlateTextBox.send_keys(self.dataGenerator.name())

        untiFuelDropBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "select[testid='fuel_type']")
        untiFuelDropBox.click()
        fuelValue = untiFuelDropBox.find_element(By.CSS_SELECTOR, "option[value='95']")
        fuelValue.click()

        untiTrailerDropBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "afaqy-custom-select[testid='tailer_id']")
        dropBoxInputBox = untiTrailerDropBox.find_element(By.CSS_SELECTOR, "input[type='text']")
        dropBoxInputBox.send_keys("TMT")

        dropBoxItemsPanel = untiTrailerDropBox.find_element(By.TAG_NAME, "ng-dropdown-panel")
        dropBoxTrailersList = dropBoxItemsPanel.find_elements(By.CSS_SELECTOR, "div[role='option']")
        while len(dropBoxTrailersList) > 1:
            for x, driverName in enumerate(dropBoxTrailersList[1:]):
                if driverName.get_attribute("innerText") == "TMT12":
                    driverName.click()
                    break
            break

        unitDriverDropBox = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "afaqy-custom-select[testid='driver_id']")
        dropBoxInputBox = unitDriverDropBox.find_element(By.CSS_SELECTOR, "input[type='text']")
        dropBoxInputBox.send_keys("driver")

        dropBoxItemsPanel = unitDriverDropBox.find_element(By.TAG_NAME, "ng-dropdown-panel")
        dropBoxDriversList = dropBoxItemsPanel.find_elements(By.CSS_SELECTOR, "div[role='option']")
        while len(dropBoxDriversList) > 1:
            for x, driverName in enumerate(dropBoxDriversList[1:]):
                if driverName.get_attribute("innerText") == "drivertest":
                    driverName.click()
                    break
            break
        # --- No Assert here

    # - Step 7 - Groups Tab : Tab index = 3
    def groupTabProcess(self, groupName):
        self.switchTab(addUnitDialogUIElement, 3)
        # ======================
        activeTabArea = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "tab[class='tab-pane active']")
        unitGroupSearchBox = activeTabArea.find_element(By.CSS_SELECTOR, "input[type='text']")
        unitGroupSearchBox.send_keys(groupName)

        groupsGridList = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "div[class='flexgridSelect']")
        groupsGridRowsSpace = groupsGridList.find_element(By.CSS_SELECTOR, "div[wj-part='cells']")
        groupsRowsList = groupsGridRowsSpace.find_elements(By.CSS_SELECTOR, "div[class='wj-row']")
        while len(groupsRowsList) > 1:
            for x, groupName in enumerate(groupsRowsList[1:]):
                if groupName.get_attribute("innerText") == groupName:
                    groupName.find_element(By.CSS_SELECTOR, "div[role='gridcell']").click()
                    break
            break
        buttonsGroupDiv = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "div[class*='assign-buttons']")
        addSingleGroupButton = buttonsGroupDiv.find_element(By.CSS_SELECTOR, "button:nth-of-type(2)")
        addSingleGroupButton.click()
        # --- No Assert here

    # - Step 8 - Fuel Consumption : Tab index = 3
    def fuelTabProcess(self):
        self.switchTab(addUnitDialogUIElement, 4)
        # ======================
        addSingleGroupButton = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "label[for='unit-fc-math-enable']")
        addSingleGroupButton.click()
        # --- No Assert here

    # - Step 9 - Sensor Tab : Tab index = 7
    def sensorTabProcess(self):
        self.switchTab(addUnitDialogUIElement, 7)
        # ======================
        activeTabArea = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "tab[class='tab-pane active']")
        addSensorButton = activeTabArea.find_element(By.TAG_NAME, "button")
        addSensorButton.click()

        addSensorDialog = addUnitDialogUIElement.find_element(By.TAG_NAME, "unit-sensor-form")

        sensorNameTextBox = addSensorDialog.find_element(By.CSS_SELECTOR, "input[formcontrolname='name']")
        sensorNameTextBox.send_keys(self.dataGenerator.name())

        sensorTypeDropBox = addSensorDialog.find_element(By.CSS_SELECTOR, "select[formcontrolname='type']")
        sensorTypeDropBox.click()
        typeValue = sensorTypeDropBox.find_element(By.CSS_SELECTOR,
                                                   "option[value='custom']")
        typeValue.click()

        sensorParamDropBox = addSensorDialog.find_element(By.CSS_SELECTOR, "select[formcontrolname='param']")
        sensorParamDropBox.click()
        paramValue = sensorParamDropBox.find_element(By.CSS_SELECTOR, "option[value='parm253']")
        paramValue.click()

        sensorShowToolTip = addSensorDialog.find_element(By.CSS_SELECTOR, "label[for='tooltip_show']")
        sensorShowToolTip.click()

        sensorMeasurmentDropBox = addSensorDialog.find_element(By.CSS_SELECTOR, "select[formcontrolname='result_type']")
        sensorMeasurmentDropBox.click()
        measurmentValue = sensorMeasurmentDropBox.find_element(By.CSS_SELECTOR, "option[value='value']")
        measurmentValue.click()

        smallModelFooter = addSensorDialog.find_element(By.TAG_NAME, "form-actions")
        saveButton = smallModelFooter.find_element(By.CSS_SELECTOR, "button:nth-of-type(1)")
        saveButton.click()
        # --- No Assert here

    # - Step 9 - Commands Tab : Tab index = 8
    def commandsTabProcess(self):
        self.switchTab(addUnitDialogUIElement, 8)
        # ======================
        activeTabArea = addUnitDialogUIElement.find_element(By.CSS_SELECTOR, "tab[class='tab-pane active']")
        addCommandsButton = activeTabArea.find_element(By.TAG_NAME, "button")
        addCommandsButton.click()

        addCommandsDialog = addUnitDialogUIElement.find_element(By.TAG_NAME, "unit-commands-form")

        commandNameTextBox = addCommandsDialog.find_element(By.CSS_SELECTOR, "input[formcontrolname='name']")
        commandNameTextBox.send_keys(self.dataGenerator.name())

        commandTypeDropBox = addCommandsDialog.find_element(By.CSS_SELECTOR,
                                                            "select[formcontrolname='protocol_command_id']")
        commandTypeDropBox.click()
        typeValue = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='custom']")))
        typeValue.click()

        commandChannelDropBox = addCommandsDialog.find_element(By.CSS_SELECTOR, "select[formcontrolname='channel']")
        commandChannelDropBox.click()
        typeValue = commandChannelDropBox.find_element(By.CSS_SELECTOR, "option[value='gprs']")
        typeValue.click()

        commandNameTextBox = addCommandsDialog.find_element(By.CSS_SELECTOR, "input[formcontrolname='param']")
        commandNameTextBox.send_keys(self.dataGenerator.name())

        smallModelFooter = addCommandsDialog.find_element(By.TAG_NAME, "form-actions")
        saveButton = smallModelFooter.find_element(By.CSS_SELECTOR, "button:nth-of-type(1)")
        saveButton.click()

    # - Step 10 - Submit Adding Unit
    def submitAddingUnit(self):
        bigModelFooter = addUnitDialogUIElement.find_element(By.TAG_NAME, "form-actions")
        saveButton = bigModelFooter.find_element(By.CSS_SELECTOR, "button:nth-of-type(1)")
        saveButton.click()

        notificationDivision = self.driver.find_element(By.TAG_NAME, "simple-notifications")
        sucessNotification = WebDriverWait(notificationDivision, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class*='success']")))
        return sucessNotification

    # - External Step - Switch Tab Function
    def switchTab(self, addUnitDialogElement, tabIndex):
        tabLists = addUnitDialogElement.find_element(By.CSS_SELECTOR, "ul[class='nav nav-tabs']")
        targetTap = tabLists.find_element(By.CSS_SELECTOR,
                                          f"li:nth-of-type({tabIndex})")  # ---- needed tab index (Needed tab)
        targetTap.click()

