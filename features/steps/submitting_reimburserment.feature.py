from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.project1_home import Project1HomePage


@given(u'The user is Signed in')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('http://localhost:5500/')
    sleep(3)
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.username_input().send_keys('Robert')
    sleep(3)
    project1_home_page.password_input().send_keys('Stark')
    sleep(3)
    project1_home_page.login_button().click()
    sleep(3)


@given(u'The user presses the courses tab')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.courses_tab().click()
    sleep(5)


@when(u'The user fills the form for a course')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.event_description_input().send_keys('Revature Training')
    project1_home_page.grade_required_input().send_keys('B')
    project1_home_page.cost_input().send_keys('500')
    project1_home_page.location_input().send_keys('Florida')
    project1_home_page.work_justification_input().send_keys('Training for new job!')
    project1_home_page.time_input().send_keys('1000am')
    project1_home_page.start_date_input().send_keys('08052021')
    project1_home_page.event_type_input().select_by_visible_text('University Course')
    sleep(8)


@when(u'The user presses the submit course button')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.submit_course_btn().click()
    sleep(5)


@then(u'The submitted record course appears')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    assert  project1_home_page.submit_course_text().text =='Record inserted'
