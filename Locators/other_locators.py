from playwright.sync_api import sync_playwright
import time

with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   # open a new page/tab in ur recomended browser

    # open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_22/playwright_prac/other_locators.html")

    page.get_by_role("button",name="Submit").click()

# get by label - Username
    username = page.get_by_label("Username")
    username.fill("admin")
    # get by label - Password
    password = page.get_by_label("Password")
    password.fill("password")
    time.sleep(3)

    # get by role
    page.get_by_role("button", name="Login").click()

    time.sleep(3)

    # get by text
    text1 = page.get_by_text("Welcome to Playwright automation practice").is_visible()
    print(text1)
    time.sleep(3)
    page.get_by_text("Accept Terms and Conditions").click()
    time.sleep(3)

    # get by placeholder
    email = page.get_by_placeholder("Enter your email")
    email.fill("test@example.com")
    search = page.get_by_placeholder("Search here")
    search.fill("Playwright")

    time.sleep(3)

    browser.close()