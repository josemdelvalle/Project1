from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


class Project1HomePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username_input(self):
        return self.driver.find_element_by_id('usernameInput')

    def password_input(self):
        return self.driver.find_element_by_id('passwordInput')

    def login_button(self):
        return self.driver.find_element_by_id('loginButton')
        # return self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')

    def login_out(self):
        return self.driver.find_element_by_id('searchInput')

    def courses_tab(self):
        return self.driver.find_element_by_id('courses_tab')

    def event_description_input(self):
        return self.driver.find_element_by_id('description')

    def grade_required_input(self):
        return self.driver.find_element_by_id('requiredGrade')

    def cost_input(self):
        return self.driver.find_element_by_id('inputCost')

    def location_input(self):
        return self.driver.find_element_by_id('inputLocation')

    def work_justification_input(self):
        return self.driver.find_element_by_id('workJustification')

    def time_input(self):
        return self.driver.find_element_by_id('courseTime')

    def start_date_input(self):
        return self.driver.find_element_by_id('startDate')

    def event_type_input(self):
        return Select(self.driver.find_element_by_id('eventType'))

    def login_message(self):
        return self.driver.find_element_by_id('loginMessage')

    def submit_course_btn(self):
        return self.driver.find_element_by_id('submitCourseBtn')

    def submit_course_text(self):
        return self.driver.find_element_by_id('subitCourseMessage')

    def get_courses_button(self):
        return self.driver.find_element_by_id('getCoursesBtn')

    def approve_course_input(self):
        return self.driver.find_element_by_id('approveCourseInput')

    def approve_course_btn(self):
        return self.driver.find_element_by_id('approveCourseBtn')

    def approve_check(self):
        return self.driver.find_element_by_xpath('//*[@id="courseTableBody"]/tr[1]/td[14]')
