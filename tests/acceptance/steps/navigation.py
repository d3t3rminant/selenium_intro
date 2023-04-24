from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)

@then('I am on the blog page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert context.driver.current_url == page.url


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@then('I am on the homepage')
def step_impl(context):
    page = HomePage(context.driver)
    assert context.driver.current_url == page.url


@given("I am on the new post page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://127.0.0.1:5000/post")


