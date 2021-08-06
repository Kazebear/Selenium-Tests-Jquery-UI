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

    # INTERACTIONS
    jquery_draggable = "https://jqueryui.com/draggable/"
    jquery_droppable = "https://jqueryui.com/droppable/"
    jquery_resizable = "https://jqueryui.com/resizable/"
    jquery_selectable = "https://jqueryui.com/selectable/"
    jquery_sortable = "https://jqueryui.com/sortable/"

    rsz_widg_bottom = 'ui-resizable-handle.ui-resizable-s'
    rsz_widg_left = 'ui-resizable-handle.ui-resizable-e'

    # Widgets
    jquery_accordion = "https://jqueryui.com/accordion/"


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

    # INTERACTIONS
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

    @classmethod
    def resize_widget(cls):
        driver = super().driver
        rsz_bottom = super().rsz_widg_bottom
        rsz_left = super().rsz_widg_left
        resizable = super().jquery_resizable
        driver.get(resizable)
        driver.switch_to.frame(0)
        resize_bottom = driver.find_element_by_class_name(rsz_bottom)
        resize_left = driver.find_element_by_class_name(rsz_left)
        action = ActionChains(driver)
        action.click_and_hold(resize_bottom).move_by_offset(0, 100).release().perform()
        time.sleep(2)
        action.click_and_hold(resize_left).move_by_offset(100, 0).release().perform()
        print("resized")
        time.sleep(5)

    @classmethod
    def selectable(cls):
        driver = super().driver
        slctb = super().jquery_selectable
        driver.get(slctb)
        time.sleep(5)
        driver.switch_to.frame(0)
        items = driver.find_elements_by_class_name('ui-widget-content.ui-selectee')
        for item in items:
            action = ActionChains(driver)
            action.double_click(item).perform()
            time.sleep(2)

        driver.close()

    @classmethod
    def sortable(cls):
        driver = super().driver
        srtbl = super().jquery_sortable
        driver.get(srtbl)
        time.sleep(5)
        driver.switch_to.frame(0)
        items = driver.find_elements_by_class_name('ui-state-default.ui-sortable-handle')
        for item in items:
            action = ActionChains(driver)
            action.click_and_hold(item).move_by_offset(0, 50).pause(3).release().perform()
        driver.close()

    # WIDGETS
    @classmethod
    def accordion(cls):
        driver = super().driver
        accrd = super().jquery_accordion
        driver.get(accrd)
        time.sleep(5)
        driver.switch_to.frame(0)
        action = ActionChains(driver)
        items = driver.find_elements_by_class_name\
            ("ui-accordion-header.ui-corner-top.ui-state-default.ui-accordion-icons.ui-accordion-header-collapsed.ui-corner-all")
        for item in items:
            action = ActionChains(driver)
            action.double_click(item).pause(3).perform()

        driver.close()


def testings():
    link = Selectors.jquerylink
    Selectors.driver.get(link)
    time.sleep(3)
    # not closing driver 'cus session gets deleted -> invalid session id


def testings2():
    S_Functions.accordion()


def testings3():
    S_Functions.parse_sidelinks()

# link = "https://jqueryui.com/"
# driver = webdriver.Chrome('/Users/kaze/Desktop/chromedriver/chromedriver')
# driver.get(link)
# time.sleep(5)
# driver.close()
