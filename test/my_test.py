from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClass:
    def test_mytest(self):
        driver = init_appium_driver()
        wait = WebDriverWait(driver, 30)

        wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[@resource-id='first-load-modal-close-check-box-accessibility-aware-checkbox']"))).click()
        wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH, "//*[@resource-id='first-load-modal-close-button']"))).click()
        driver.quit()


def init_appium_driver():
    options = AppiumOptions()
    options.load_capabilities(get_capabilities())

    return webdriver.Remote(get_url(), options=options)


def get_url() -> str:
    return "{protocol}://{host}:{port}{path}".format(
        protocol="https",
        host="ondemand.us-west-1.saucelabs.com",
        port="443",
        path="/wd/hub",
    )


def get_capabilities():
    capabilities = {}
    capabilities['noReset'] = True
    capabilities['fullReset'] = False
    capabilities['deviceOrientation'] = 'portrait'
    capabilities['automationName'] = 'UiAutomator2'
    capabilities['platformName'] = 'android'
    capabilities['deviceName'] = 'Samsung Galaxy S22.*'
    capabilities['platformVersion'] = '13'
    capabilities['app'] = 'storage:filename=app-release-Staging-20240228.4.apk'
    capabilities['autoGrantPermissions'] = 'true'
    capabilities['sauce:options'] = {}
    capabilities['sauce:options']['appiumVersion'] = 'latest'
    capabilities['sauce:options']['cacheId'] = 'Android-1'
    capabilities['sauce:options']['username'] = 'test'
    capabilities['sauce:options']['accessKey'] = 'test'
    capabilities['sauce:options']['enableAnimations'] = "true"
    return capabilities
