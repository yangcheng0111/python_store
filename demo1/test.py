import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Demo1:
    def __init__(self):
        self.zhaosheng = None
        self.chrome = webdriver.Chrome()
        self.chrome.implicitly_wait(5)

    def start_web2(self):
        self.zhaosheng.click()

    def start_web3(self):
        # 查找包含"党建工作"内容的元素
        dangjiangongzuo = self.chrome.find_element(By.XPATH, "//*[contains(text(), '党建工作')]")
        # 定义动作链
        actions = ActionChains(self.chrome)
        # 执行动作
        actions.move_to_element(dangjiangongzuo).click(
            self.chrome.find_element(By.XPATH, "//*[contains(text(), '党史学习教育')]")).perform()

    def baidu(self):
        self.chrome.get('https://www.baidu.com/')
        element = self.chrome.find_element(By.XPATH, '//*[@id="kw"]')
        element.send_keys('软件测试')
        element.send_keys(Keys.ENTER)

        while True:
            try:
                next = self.chrome.find_element(By.XPATH, '//*[@id="page"]/div/a[contains(.,"下一页")]')
                self.chrome.execute_script("arguments[0].scrollIntoView();", next)
                next.click()
            except:
                print('页面未加载好状态')



if __name__ == '__main__':
    demo1 = Demo1()
    demo1.baidu()
