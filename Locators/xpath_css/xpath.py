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

    #2. using tagname (//tagname[text()='value'])
    login = page.locator("//button[text()='Login']")
    login.click()
    print(login.text_content())

    #3. using contains :- mostly doing the partial match (//tagname[conatins(@attribute/text(),"value")])
    click = page.locator("//button[contains(text(),'OTP')]")
    click.click()
    print(click.text_content())

    #4 using normalize-space :- remove the unauthorized space from the text
    # //button[normalize-space() = .'login']

    #starts with :- matching some first characters

    time.sleep(5)

    browser.close()