from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json


class Selectors:
    jquerylink = "https://jqueryui.com/"
    link = ""

    # Replace driver string with your chromedriver directory
    driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
    sidelinksjson = "sidelinks.json"
    jquery_draggable = "https://jqueryui.com/draggable/"
    jquery_droppable = "https://jqueryui.com/droppable/"


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

    # DRAG METHOD
    @classmethod
    def drag(cls):
        driver = super().driver
        draggable = super().jquery_draggable
        driver.get(draggable)
        driver.switch_to.frame(0)
        drag_obj = driver.find_element_by_id('draggable')
        action = ActionChains(driver)
        action.click_and_hold(drag_obj).move_by_offset(250, 100).pause(2).move_by_offset(0, 100).release().perform()
        print("dragged")

    @classmethod
    def drag_and_drop_ontarget(cls):
        driver = super().driver
        driver.get(super().jquery_droppable)
        driver.implicitly_wait(5)
        driver.switch_to.frame(0)
        draggable = driver.find_element_by_id('draggable')
        target = driver.find_element_by_id('droppable')
        action = ActionChains(driver)
        action.drag_and_drop(draggable, target).perform()
        time.sleep(5)



def testings():
    link = Selectors.jquerylink
    Selectors.driver.get(link)
    time.sleep(3)
    # not closing driver 'cus session gets deleted -> invalid session id


def testings2():
    S_Functions.drag_and_drop_ontarget()


def testings3():
    S_Functions.parse_sidelinks()

# link = "https://jqueryui.com/"
# driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
# driver.get(link)
# time.sleep(5)
# driver.close()
