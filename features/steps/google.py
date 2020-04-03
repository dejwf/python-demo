
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *


@given('open browser')
def step_impl(context):
     context.browser = webdriver.Firefox(executable_path=r'.\geckodriver-v0.26.0-win64\geckodriver.exe')

@when('navigate to google')
def step_impl(context):
    context.browser.get('https://www.google.com')
    assert 'Google' in context.browser.title
    print("should be on the index site")
    assert True is not False

@then('search vlkancice')
def step_impl(context):
    context.browser.implicitly_wait(3)
    print("after wait")
    elem = context.browser.find_element_by_name('q')  # Find the search box
    print("should get  the element")
    elem.send_keys('Vlkancice' + Keys.RETURN)
    print("should send keystrokes")
    assert context.failed is False

@then('vlkancice are in the search result page (SERP)')
def step_impl(context):
    context.browser.implicitly_wait(3)
    time.sleep(3)
    context.browser.quit()