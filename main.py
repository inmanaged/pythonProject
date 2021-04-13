# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import pyautogui

#Chrome실행
options = Options()
options.add_argument('--start-fullscreen')
driver = webdriver.Chrome("C:\\Users\inmanaged\PycharmProjects\chromedriver.exe", chrome_options=options)

#엣지실행
#driver = webdriver.Edge(excutable_path='')
#IE실행
#driver = webdriver.Ie(executable_path='')

#URL이동
driver.get("https://store.musinsa.com/app/")

time.sleep(4)

#로그인버튼누름
driver.find_element_by_xpath("//*[@id=\"default_top\"]/div[3]/button").click()

time.sleep(3)

#아이디입력
driver.find_element_by_xpath("/html/body/div[1]/div/form/input[2]").send_keys('inmanaged')


time.sleep(1)

#패스워드입력
driver.find_element_by_xpath("/html/body/div[1]/div/form/input[3]").send_keys('dmEmadl337')
time.sleep(1)

#로그인버튼누름
driver.find_element_by_xpath("/html/body/div[1]/div/form/button").click()
time.sleep(2)

#마이페이지 누름
driver.find_element_by_xpath("//*[@id=\"default_top\"]/div[3]/div[4]/a").click()
time.sleep(3)

#무신사페이 관리 누름
driver.find_element_by_xpath("/html/body/div[3]/div[2]/nav/dl/dd[9]/a").send_keys(Keys.CONTROL + "\n") #탭으로열기
#driver.find_element_by_xpath("/html/body/div[3]/div[2]/nav/dl/dd[9]/a").send_keys("\n") #팝업으로열기
time.sleep(3)

#열린탭으로 제어포커싱 변경
driver.switch_to.window(driver.window_handles[1])
#driver.switch_to.frame('__tosspayments_openpay_iframe_2__')
#driver.find_element_by_xpath("//*[@id=\"__next\"]/div[1]/ul/li[1]/div[2]/div[1]/span").click()
#time.sleep(2)
#driver.find_element_by_xpath("//*[@id=\"button16\"]").click()

driver.switch_to.frame('__tosspayments_openpay_iframe_2__')
register_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\register.png')
pyautogui.click(register_location)
time.sleep(1)

#카드정보입력
#6048-2351-0993-2155
#04/21
#136
#1944

print(driver.window_handles)

time.sleep(3)
register_and_delete_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\register_and_delete.png')
pyautogui.click(register_and_delete_location)
time.sleep(1)

register_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\register.png')
pyautogui.click(register_location)
time.sleep(1)

#driver.find_element_by_id("text-field-line-36").click()
time.sleep(1)

#카드번호 입력
input_card_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\input_card.png')
pyautogui.click(input_card_location)

#1초에 한번씩 키패드 입력
pyautogui.typewrite("60482351", interval=0.5)


time.sleep(1)
num0_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\0.png')
pyautogui.click(num0_location)
num9_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\9.png')
pyautogui.click(num9_location)
pyautogui.click(num9_location)
num3_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\3.png')
pyautogui.click(num3_location)
#driver.find_element_by_id("text-field-line-35").click()
time.sleep(1)
num2_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\2.png')
pyautogui.click(num2_location)
num1_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\1.png')
pyautogui.click(num1_location)
num5_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\5.png')
pyautogui.click(num5_location)
pyautogui.click(num5_location)
time.sleep(1)

#유효기간 입력 04/21
#driver.find_element_by_id("text-field-line-30").click()
num0_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\0.png')
pyautogui.click(num0_location)
num4_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\4.png')
pyautogui.click(num4_location)
num2_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\2.png')
pyautogui.click(num2_location)
num1_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\1.png')
pyautogui.click(num1_location)
time.sleep(1)

#CVC 입력 136
#driver.find_element_by_id("text-field-line-28").click()
num1_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\1.png')
pyautogui.click(num1_location)
num3_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\3.png')
pyautogui.click(num3_location)
num6_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\6.png')
pyautogui.click(num6_location)
time.sleep(1)

#카드비번입력 19(비씨는 2자리)
#driver.find_element_by_id("text-field-line-26").click()
num1_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\1.png')
pyautogui.click(num1_location)
num9_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\9.png')
pyautogui.click(num9_location)
time.sleep(1)

#확인
register_confirm = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\register_confirm.png')
pyautogui.click(register_confirm)
time.sleep(3)

#등록카드 삭제
delete_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\delete.png')
pyautogui.click(delete_location)
time.sleep(3)

#time.sleep(1)
delete_button_location = pyautogui.locateOnScreen('C:\\Users\inmanaged\PycharmProjects\pythonProject\image\\delete_button.png')
pyautogui.click(delete_button_location)
