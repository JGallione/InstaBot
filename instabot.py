import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from getpass import getpass

#--Login Credentials--#
username = input("Username:")
password = getpass("Password:") 

#--Amount of Users Accepted--#
count = int(input("How Many Opt-Ins?:"))

#--Webdriver Settings--#
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#chromedriver location below EDIT THE PATH
driver = webdriver.Chrome('PATH/TO/chromedriver', options=options)

#--Text--#
User_Request_1 = "a"
Instabot_reply_1 = "b"
Instabot_reply_2_DoubleSEND = "c"


def login():
    driver.get('https://www.instagram.com/')
    time.sleep(1)
    #Login Form Locations#
    usernamefield = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
    passwordfield = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
    loginbutton = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]')
    #Sending Credentials and Login#
    usernamefield.send_keys(username)
    passwordfield.send_keys(password)
    loginbutton.click()
    time.sleep(5)

def dms():
    #Get Dms#
    driver.get('https://www.instagram.com/direct/inbox/')
    time.sleep(3)
    #Checking for notification cookie you see when not headless#
    try:
        notnow = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[3]/button[2]')
        notnow.click()
        print("\n Instabot is Live!\n")
        print("---Logs---")
    except:
        print("\n Instabot is Live!\n")
        print("---Logs---")

def msgr(count):
    opt_in_list = []

    while len(opt_in_list) < count:
        msgs = driver.find_elements_by_xpath('.//span[@class = "_7UhW9   xLCgt       qyrsm KV-D4           se6yk        "]')
        for msg in msgs:
            try:
                msgtext = msg.text
            except:
                msgtext = "Typing... or Multi-msg"

            if msgtext.lower() == User_Request_1:
                msg.click()
                time.sleep(2)

                chatbox = driver.find_element_by_tag_name('textarea')
                IGTag = driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div')
                currenttime = time.strftime("%H:%M:%S", time.localtime())

                for ig in IGTag:
                    if ig.text not in opt_in_list:
                        chatbox.send_keys(Instabot_reply_1 + Keys.RETURN)
                        print("New Opt_In!: " + ig.text + " | " + str(currenttime))                        
                        opt_in_list.append(ig.text)
                        driver.back()
                    else:
                        chatbox.send_keys(Instabot_reply_2_DoubleSEND) + Keys.RETURN)
                        print(ig.text + " Tried to reOpt-In" + " | " + str(currenttime))
                        driver.back()

            driver.refresh()
            time.sleep(2)

    print("\n")
    print("Number of Opt-Ins:" + str(len(opt_in_list)))
    print(*opt_in_list, sep = ", ") 
    print("\n")

login()
dms()
msgr(count)
driver.close()
