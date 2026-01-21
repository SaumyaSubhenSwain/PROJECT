

# import playwright's synchronous api
# sync_playwright() manages browser life cycle

from playwright.sync_api import sync_playwright

# Chromium - launch
# headless=False ----> browser visible
# with the help of with statement open the context manager of playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   # open a new page/tab in your recommended browser

    # open a link and hit in api and call the url
    page.goto("https://www.facebook.com/login/")

    page.locator("#email").fill("babuli@gmail.com")
    page.locator("#pass").fill("Babuli@123")
    page.locator("#loginbutton").click()


    browser.close() #close the browser
