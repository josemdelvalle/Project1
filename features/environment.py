from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.project1_home import Project1HomePage

# All setup and teardown functions must go in this file.
# These functions must be named using behave's conventions


def before_all(context):
    driver: WebDriver = webdriver.Chrome('C:/Users/JMDel/Documents/Revature/Selenium/chromedriver.exe')
    project1_home_page = Project1HomePage(driver)
    context.driver = driver
    context.project1_home_page = project1_home_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")

