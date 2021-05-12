from time import sleep
from behave import when, given, then
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.project1_home import Project1HomePage


@given('The User is on the Project 1 LogIn Page')
def get_to_home(context):
    driver: WebDriver = context.driver
    driver.maximize_window()
    driver.get('http://localhost:5500/')
    sleep(5)


@when('The user types the {username} in the username bar')
def write_username(context, username):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.username_input().send_keys(username)
    sleep(5)


@when('The user types the {password} in the password bar')
def write_password(context, password):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.password_input().send_keys(password)
    sleep(5)


@when('Presses the submit button')
def step_impl(context):
    project1_home_page: Project1HomePage = context.project1_home_page
    project1_home_page.login_button().click()
    sleep(5)


@then('The Logged in {message} appears')
def step_impl(context, message):
    project1_home_page: Project1HomePage = context.project1_home_page
    assert project1_home_page.login_message().text == message
