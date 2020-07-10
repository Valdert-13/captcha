from selenium import webdriver
import time
import random
from main import chec_dir
from config import *


download_path = os.path.join(DATA_PATH, 'download/')
chec_dir(download_path)
driver = webdriver.Firefox(executable_path=r'C:\Users\LSK-17\Desktop\geckodriver-v0.26.0-win64\geckodriver.exe')
driver.get("https://rosreestr.ru/wps/portal/online_request")

count = COUNT_IMG_TRAIN + COUNT_IMG_TEST - len(os.listdir(download_path))

print(count)

for _ in range (count):
    scr = time.time()
    with open(download_path + 'filename_{scr}.png', 'wb') as file:
        file.write(driver.find_element_by_css_selector("#captchaImage2").screenshot_as_png)
    act = driver.find_element_by_class_name('v-button-caption.span_links')
    act.click()
    sleep_time = random.randint(1, 5)
    time.sleep(sleep_time)

driver.close()