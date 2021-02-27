import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from getpass import getpass
import emoji

#--Login Credentials--#
print("Logging in with...")
username = input("Username:")
password = getpass("Password:") 

#--Amount of Users Accepted--#
count = int(input("How Many Opt-Ins?:"))

#--Webdriver Settings--#
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
#chromedriver location below
driver = webdriver.Chrome('/Users/josephgallione/Documents/code/instadmbot/chromedriver', options=options)

#--Text--#
Instabot_reply_1 = "Hey! Whaaazzzup?"
Instabot_reply_2 = "?hello"
Instabot_reply_3 = emoji.emojize("Great content! Fantastic (y) But look at dis...")
Instabot_reply_4 = emoji.emojize("Im doin me lol how are you?")
Instabot_reply_5 = emoji.emojize("Just send me a dank meme already")
Instabot_reply_6 = emoji.emojize("  ")
User_Request_1 = "a"
Instabot_reply_1 = "b"
Instabot_reply_2_DoubleSEND = "c"

def send_meme(ig):
    driver.get('https://www.instagram.com/p/CK7QjpdL6nM/')
    time.sleep(2)
    sendbutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[3]/button')
    sendbutton.click()
    time.sleep(2)
    searchbutton = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
    time.sleep(2)
    searchbutton.send_keys(ig)
    time.sleep(3)
    usersend = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/div')
    usersend.click()
    
    sendfinal = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button')
    sendfinal.click()

def login():
    driver.get('https://www.instagram.com/')
    time.sleep(3)
    #Login Form Locations#/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input
    usernamefield = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
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
            msgtextlower = msgtext.lower()
            msgtextarray = msgtextlower.split(" ")
            print(msgtextarray)
            GreetingsArray = ["hey", "hello", "yo", "hi", "joey"]
            howareyouarray = ["how", "are", "you"]
            if any(word in GreetingsArray for word in msgtextarray):
                msg.click()
                time.sleep(2)
                #hello
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
            
            elif all(word in howareyouarray for word in msgtextarray):#FIX THIS IT ONLY TAKES EXACT BUT THATS SHI
                msg.click()
                time.sleep(2)

                chatbox = driver.find_element_by_tag_name('textarea')
                IGTag = driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div')
                currenttime = time.strftime("%H:%M:%S", time.localtime())
                for ig in IGTag:
                    chatbox.send_keys(Instabot_reply_4 + Keys.RETURN) 
                    print("howyadoinback? " + ig.text + " | " + str(currenttime))
                    driver.back()
            elif msgtextlower == "sent a post":
                msg.click()
                

                chatbox = driver.find_element_by_tag_name('textarea')
                IGTag = driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div')
                currenttime = time.strftime("%H:%M:%S", time.localtime())
                time.sleep(2)
                chatbox.send_keys(Instabot_reply_3 + Keys.RETURN)
                for ig in IGTag:
                        ig = ig.text
                        send_meme(ig)
                        print("Meme Alert!: " + ig + " | " + str(currenttime))                        
                        
                        driver.back()
            else:
                msg.click()

                chatbox = driver.find_element_by_tag_name('textarea')
                IGTag = driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div/div')    
                currenttime = time.strftime("%H:%M:%S", time.localtime())
                print(msgtext)
                time.sleep(3)
                chatbox.send_keys(Instabot_reply_5 + Keys.RETURN)
            driver.refresh()
            time.sleep(7)
            print(msgtext)
            


    print("\n")
    print("Number of Opt-Ins:" + str(len(opt_in_list)))
    print(*opt_in_list, sep = ", ") 
    print("\n")

login()
dms()
msgr(count)
driver.close()