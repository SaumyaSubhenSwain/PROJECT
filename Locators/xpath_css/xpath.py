import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   # open a new page/tab in your recommended browser

    # open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_22/playwright_prac/Locators/xpath_css/xpath_prac.html")

    #1. using attribute (//tagname[@attribute='value'])
    username = page.locator("//input[@name='username']")
    username.fill("My name is saumya")


    time.sleep(5)

    browser.close()