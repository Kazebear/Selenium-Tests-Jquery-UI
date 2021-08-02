from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json


class Selectors:
    jquerylink = "https://jqueryui.com/"
    link = ""
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    sidelinksjson = "sidelinks.json"


class S_Functions(Selectors):

    @classmethod
    def parse_sidelinks(cls):
        driver = super().driver
        driver.get(super().jquerylink)
        sidelinks = super().sidelinksjson

        with open(sidelinks, 'r') as s:
            sidelinks = json.load(s)
            for name in sidelinks:
                string = "".join(name)
                driver.implicitly_wait(3)
                sidelinks = driver.find_element_by_link_text(string)
                driver.implicitly_wait(3)
                sidelinks.send_keys(Keys.RETURN)
                string.replace(string, "")
            s.close()

        driver.close()


def testings():
    link = Selectors.jquerylink
    Selectors.driver.get(link)
    time.sleep(3)
    # not closing driver 'cus session gets deleted -> invalid session id


def testings2():
    S_Functions.parse_sidelinks()

# link = "https://jqueryui.com/"
# driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
# driver.get(link)
# time.sleep(5)
# driver.close()
