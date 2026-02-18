from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   # open a new page/tab in ur recomended browser

    # open a link and hit in api and call the url
    page.goto("")