from time import sleep
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import random
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class whatsapp():
    def message(self):
        df = pd.read_csv(BASE_DIR+"/whatspp/phone.csv")
        phone_no = df["Number"].tolist()
        namee = df['Name'].tolist()
        self.driver = webdriver.Chrome(BASE_DIR+"/whatspp/chromedriver_85")
        self.driver.get("https://web.whatsapp.com/")
        first=random.randint(12,20)
        sleep(first)
        print(phone_no)
        for num in phone_no:
            try:
                innn=phone_no.index(num)
                self.driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(num))
                sleep(first)
                link = 'https://www.linkedin.com/in/troycrema/'
                msg=self.driver.find_element_by_css_selector('._1hRBM > div:nth-child(2)')
                text1 = "Hi " + str(namee[innn]) + ", my name is Lou Tempesta and I am a Senior Director at Cozzini Bros. At Cozzini, we partner with the best chefs in America. I noticed that you've been sharing your thoughts on culinary matters on Twitter and thus I wanted to reach out to you personally. We provide America's most discerning chefs with best in class knife sharpening services. We make sure your tools match your unparalleled professionalism. I would love to discuss how we can make you even more effective in the kitchen and add real value to your passion."
                text2 = "Send me a quick reply letting me know you're interested in learning more."
                text3 = "Talk soon,"
                text4 = "Lou"
                text5 = "PS - I sent a link to my LinkedIn above (so you know I am not a BOT)"
                msg.send_keys(link)
                self.driver.find_element_by_class_name("_2Ujuu").click()
                sleep(2)
                msg.send_keys(Keys.SHIFT + Keys.ENTER)
                msg.send_keys(text1)
                msg.send_keys(Keys.SHIFT + Keys.ENTER)
                msg.send_keys(text2)
                msg.send_keys(Keys.SHIFT + Keys.ENTER)
                msg.send_keys(text3)
                msg.send_keys(Keys.SHIFT + Keys.ENTER)
                msg.send_keys(text4)
                msg.send_keys(Keys.SHIFT + Keys.ENTER)
                msg.send_keys(text5)
                msg.send_keys(Keys.SHIFT + Keys.ENTER)
                sleep(1)
                self.driver.find_element_by_class_name("_2Ujuu").click()
                second = random.randint(12, 18)
                sleep(second)
                print(num," msg send")
            except:
                pass
a=whatsapp()
a.message()
