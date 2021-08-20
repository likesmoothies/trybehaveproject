from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launcbrowser(context):
    context.driver = webdriver.Chrome()

@when('open the page')
def openpage(context):
    context.driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

@Then('Verify the login page')
def verifyloginpage(context):
    status = context.driver.find_element('xpath',"//h1[contains(text(),'Admin area demo')]").is_displayed()
    assert status is True

@Then('Close browser')
def closedriver(context):
    context.driver.close()