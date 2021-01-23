from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "/Users/Devlopment/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=2376902595&f_LF=f_AL&geoId=92000001&keywords=ios%20developer&location=Remote")

# signIn

sign_in = driver.find_element_by_class_name("cta-modal__primary-btn")

link = sign_in.get_attribute("href")

print(link)
driver.get(link)
time.sleep(5)
email_field = driver.find_element_by_name("session_key")
password_field = driver.find_element_by_name("session_password")

email_field.send_keys("")
password_field.send_keys("")

sing_in_btn = driver.find_element_by_css_selector("div .login__form_action_container ")

sing_in_btn.click()
time.sleep(10)

list_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
print(list_jobs)



for listing in list_jobs:
    listing.click()
    time.sleep(2)
    try:
        job = driver.find_element_by_css_selector(".jobs-s-apply button")
        job.click()
        time.sleep(5)
    except NoSuchElementException:
        print("No apply job btn foundjob button not found")
        continue
    else:
        try:
            phone_input = driver.find_element_by_css_selector(".fb-single-line-text__input")
        except:
            print("no phone input")
            continue
        else:
            if phone_input.text == "":
                phone_input.send_keys("")

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()
            time.sleep(2)
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

