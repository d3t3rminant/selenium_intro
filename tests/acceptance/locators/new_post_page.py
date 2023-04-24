from selenium.webdriver.common.by import By

class NewPostPageLocators:
    NEW_POST_FORM = (By.ID, "post-form")
    INPUT_TITLE = (By.ID, "title")
    INPUT_CONTENT = (By.ID, "content")
    BUTTON_SUBMIT = (By.ID, "create-post")
    NAVIGATION_BLOG_LINK = (By.ID, "blog-link")