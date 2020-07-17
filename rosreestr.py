from selenium import webdriver
import time
import PySimpleGUI as sg
from PIL import Image
import random
from config import *

def download_cuptcha_rosreestr(path, count):
    """Скачиваем изображения с росреестра"""
    driver = webdriver.Firefox(executable_path=r'C:\Users\LSK-17\Desktop\geckodriver-v0.26.0-win64\geckodriver.exe')
    driver.get("https://rosreestr.ru/wps/portal/online_request")

    for _ in range (count):
        scr = time.time()
        with open(download_path + f'filename_{scr}.png', 'wb') as file:
            file.write(driver.find_element_by_css_selector("#captchaImage2").screenshot_as_png)
        act = driver.find_element_by_class_name('v-button-caption.span_links')
        act.click()
        sleep_time = random.randint(1, 5)
        time.sleep(sleep_time)

    driver.close()

def inputFilenameLayout(displayImage):
    layout = [
                [displayImage],
                [sg.InputText(key="Answer", do_not_clear=False)],
                [sg.Button('Delete', button_color=('red','white')),
                                       sg.Button('Rename', button_color=sg.COLOR_SYSTEM_DEFAULT)]
    ]
    return layout

def rename_captcha (DATASET_PATH_TEST=DATASET_PATH_TEST):
    """Реализуем интерфейс для переименование изображений с капчей"""
    sg.theme('DarkAmber')
    list_name = os.listdir(download_path)

    displayImage = sg.Image(download_path + list_name[0] , key="imageContainer")


    inputWindow = sg.Window("[{}/{}] Please Input - {}".format(1, len(list_name), list_name[0]),
                            inputFilenameLayout(displayImage))

    index = 0
    while True:

        newFilename = ""
        response = {}
        event, response = inputWindow.Read()

        newFilename = response["Answer"]

        if event == "Delete":
            for i in list_name: os.remove(i)
            index -= 1


        elif event == "Rename" and newFilename != "":
            im = Image.open(download_path + list_name[index])
            rgb_im = im.convert('RGB')
            rgb_im.save(DATASET_PATH_TEST + newFilename + '_' + str(random.randint(0, 100)) + '_.jpg')
            index += 1

        if index >= len(list_name):
            break

        inputWindow.FindElement("imageContainer").Update(download_path + list_name[index])
        inputWindow.TKroot.title("[{}/{}] Please input - {}".format(index + 1, len(list_name), list_name[index]))

    inputWindow.Close()

    sg.Window("Finished!", [[sg.Text("Finished updating {} image labels.".format(len(list_name)))], [sg.OK()]]).Read()

