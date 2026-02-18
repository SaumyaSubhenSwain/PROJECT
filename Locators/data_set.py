import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()   # open a new page/tab in your recommended browser

    # open a link and hit in api and call the url
    page.goto("file:///D:/Project/TREENETRACLASSNOTES/TREENETRA_AT_22/playwright_prac/data_set.html")
    expected_res = "Selected User ID: 101 | Name: Saumya"

    time.sleep(5)

    page.get_by_test_id("101").click()
    actual_res = page.locator("#output").text_content()
    print(actual_res)

    #verification
    '''if expected_res==actual_res:
        print("PASS")
    else:
        print("FAIL")'''

    #validation
    assert expected_res == actual_res , f"test got failed"

    browser.close() #close the browser