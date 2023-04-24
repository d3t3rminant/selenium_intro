from behave import *

from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed() # actually visible, not only present

@step('The title tag has content "(.*)"')
def step_impl(context, expected_page_title):
    page = BasePage(context.driver)
    assert page.title.text == expected_page_title

@then('There is a posts section on the blog page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()

@then('I can see there is a "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [p for p in page.posts] # if p.text == title
    assert len(posts_with_title) > 0
    assert all([post.is_displayed() for post in posts_with_title])