from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import parameters


class MyClass():
    def __init__(self):

        self.id = parameters.userrr
        print(str(self.id))
        sleep(2)
        self.password = parameters.passs
        print(str(self.password))
        sleep(2)
        # loading chrome driver
        self.driver = webdriver.Chrome('/chromedriver_linux64/chromedriver')

    def csv_tolist(self):
        df = pd.read_csv('/American1.csv')
        list2 = df['screen_name'].to_list()
        list3 = df['name'].to_list()
        return list2,list3

    def login(self):
        driver=self.driver
        driver.get('https://twitter.com/login')
        sleep(2)
        driver.find_element_by_xpath("//input[contains(@name,'session[username_or_email]')]").send_keys(str(self.id))
        sleep(1)
        driver.find_element_by_xpath("//input[contains(@name,'session[password]')]").send_keys(str(self.password))
        sleep(1)
        sign_in_button = driver.find_element_by_xpath('//*[@role="button"]')
        sign_in_button.click()

    def message(self):
        send=3968
        i=45495
        driver = self.driver
        list11,list12=self.csv_tolist()
        # print(list11,list12,'======================')23802
        list222 = list12[62268:]
        list111=list11[62268:]
        print(list111, '======================')
        for countt in list111:
            try:
                driver.get('https://twitter.com/messages/compose?')
                sleep(5)
                driver.find_element_by_xpath("//input[contains(@data-testid,'searchPeople')]").send_keys(str(countt))
                counter=list111.index(countt)
                print(counter +i,"====",countt)
                sleep(2)

                driver.find_element_by_xpath("//*[@class='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci']").click()
                sleep(5)

                driver.find_element_by_xpath("//*[@class='css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-19u6a5r r-15ysp7h r-gafmid r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']").click()

                sleep(2)
                text1 = "Hi, " +  str(list222[counter])+ "! We're making AI open source for everyone! Get insights into all the codes and some really useful AI topics on YouTube channel "
                text2="Do visit our channel & don't forget to Like, Share and Subscribe!"

                sleep(1)
                driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerSendButton')]").click()
                driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(text1)
                driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(Keys.SHIFT + Keys.ENTER)
                driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(Keys.SHIFT + Keys.ENTER)
                driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(text2)
                driver.find_element_by_xpath("//div[contains(@data-testid,'dmComposerTextInput')]").send_keys(Keys.ENTER)
                sleep(3)
                send = send + 1
                print(send)
            except:
                pass

        print("**************Total send***************")
        print(send)
        # print(counter, "====", countt)


aa=MyClass()
# function for login
aa.login()
# function for message
aa.message()


