from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.project1_home import Project1HomePage


@given(u'The User is logged in and in the courses tab')
def login_go_to_courses(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('http://localhost:5500/')
    sleep(3)
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.username_input().send_keys('Lee')
    sleep(3)
    project1_home_page.password_input().send_keys('Sin')
    sleep(3)
    project1_home_page.login_button().click()
    sleep(3)
    project1_home_page.courses_tab().click()
    sleep(3)


@when(u'The user presses the get courses tab')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.get_courses_button().click()
    sleep(10)


@when(u'The user approves the course')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.approve_course_input().send_keys('132')
    sleep(1)
    project1_home_page.approve_course_btn().click()
    sleep(5)
    project1_home_page.get_courses_button().click()
    sleep(5)



@then(u'The submitted record appears approved')
def step_impl(context):
    # project1_home_page: Project1HomePage = context.project1_home_page
    # project1_home_page.
    pass
