from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.driver = BasePage.browser()
    page = HomePage(context.driver)
    context.driver.get(page.url)

@given('I am on the blogpage')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    context.driver = BasePage.browser()
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    # context.driver = webdriver.Chrome()
    context.driver = BasePage.browser()
    page = NewPostPage(context.driver)
    context.driver.get(page.url)

@then('I am on the blogpage')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I quit the driver')
def step_impl(context):
    context.driver.quit()

@Given("I am on google page")
def step_impl(context):
    context.driver = BasePage.browser()
    context.driver.get("https://www.geeksforgeeks.org/")

@Then("Title is shown on the page")
def step_impl(context):
    assert context.driver.title == "GeeksforGeeks | A computer science portal for geeks"

