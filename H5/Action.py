import hashlib
import json
import os
import socket
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import cv2
import configparser
import sys
import numpy as np


class config:

    @staticmethod
    def getConfig(path, section, key):
        """
        加载配置文件
        :param path:
        :param section:
        :param key:
        :return:
        """
        config = configparser.ConfigParser()
        # path = os.path.split(os.path.realpath(__file__))[0] + '/H5.conf'
        config.read(path)
        return config.get(section, key)

    @staticmethod
    def setConfig(path, section, key, value):
        """
        更新页面版本
        :param path:
        :param section:
        :param key:
        :param value:
        :return:
        """
        config = configparser.ConfigParser()
        config.read(path)
        config.set(section, key, value)
        with open(path, "w") as f:
            config.write(f)
        return config.get(section, key)

    @staticmethod
    def getOptions(section):
        """
        加载配置文件
        :param section:
        :return:
        """
        config = configparser.ConfigParser()
        path = os.path.split(os.path.realpath(__file__))[0] + '/H5.conf'
        config.read(path)
        return config.options(section)


class H5Check:

    def __init__(self, h5_url):
        # 创建 WebDriver 对象，指明使用chrome浏览器驱动
        self.platform = sys.platform
        if "win" in self.platform:
            self.chrome_options = Options()
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--disable-dev-shm-usage')
            self.chrome_options.add_argument('--headless')
            self.wd = webdriver.Chrome(r'C:\Users\xiaor\Desktop\chromedriver.exe', chrome_options=self.chrome_options)
            self.wd = webdriver.Chrome(r'C:\Users\xiaor\Desktop\chromedriver.exe')
        else:
            self.chrome_options = Options()
            self.chrome_options.add_argument('--no-sandbox')
            self.chrome_options.add_argument('--disable-dev-shm-usage')
            self.chrome_options.add_argument('--headless')
            self.wd = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=self.chrome_options)
        self.wd.delete_all_cookies()
        self.wd.implicitly_wait(10)
        self.wd.get(h5_url)
        time.sleep(3)

    def __str__(self):
        return self.wd.title

    def quit(self):
        self.wd.close()
        self.wd.quit()

    def refresh(self):
        self.wd.delete_all_cookies()
        self.wd.refresh()
        print("page refresh...")
    def click(self, element):
        """
        根据页面元素实现点击页面按钮
        :param element:
        :return:
        """
        # try:
        element = self.wd.find_element_by_css_selector(element)
        element.click()
        time.sleep(5)
        # except Exception as e:
        #     # print(e)
        #     # self.quit()
        #     # exit()
        #     return 0

    def collect_img(self, element):
        """
        根据页面元素提取img url
        :param element:
        :return:
        """
        # try:
        img_url = self.wd.find_element_by_css_selector(element).get_attribute("src")
        print(img_url)
        return img_url
        # except Exception as e:
        #     print(e)
        #     # self.quit()
        #     # exit()
        #     return 0

    def send_comments(self, element, content):
        """
        向客服提交意见
        :param element
        :param content
        """
        try:
            self.wd.find_element_by_css_selector(element).send_keys(content)
            time.sleep(3)
        except Exception as e:
            print(e)
            self.quit()
            exit()

    def outerHTML(self, element):
        """
        根据页面元素获取html
        :param element:
        :return:
        """
        try:
            html = self.wd.find_element_by_css_selector(element).get_attribute("outerHTML")
            print(html)
        except Exception as e:
            print(e)
            self.quit()
            exit()

    def screenshot(self, path, img_name):
        """
        屏幕截图，根据action 命名图片名称
        :param path:
        :param img_name:
        :return:
        """
        try:
            self.wd.get_screenshot_as_file(path + img_name + '.png')
            print(path)
        except Exception as e:
            print(e)
        #     # self.quit()
        #     # exit()
        #     return 0

    def screebshot_ele(self, element, path, name):
        """
        元素截图
        :param element:
        :param path:
        :param name:
        :return:
        """
        html = self.wd.find_element_by_css_selector(element)
        html.screenshot(path + name + '.png')
        # png = html.screenshot_as_png
        # with open(path + name + '.png', 'wb') as f:
        #     f.write(png)
        # f.close()



    def get_text(self, element):
        """
        获取文本
        :param element:
        :return:
        """
        text = self.wd.find_element_by_css_selector(element).text
        return text

    def get_tag_name(self, element):
        """
        获取标签名称
        :param element:
        :return:
        """
        tag_name = self.wd.find_element_by_css_selector(element).tag_name
        return tag_name

    def get_attribute(self, element, name):
        """
        获取元素其他属性
        :param element:
        :param name:
        :return:
        """
        attribute = self.wd.find_element_by_css_selector(element).get_attribute(name)
        return attribute


class ImgCheck:

    @staticmethod
    def download_img(img_url, path, img_name):
        """
        下载img
        :param path:
        :param img_url:
        :param img_name:
        :return:
        """
        print(img_url)
        r = requests.get(img_url, stream=True)
        print(r.status_code)
        if r.status_code == 200:
            open(path + img_name, 'wb').write(r.content)
            print("done")
        else:
            alarm = AlarmDingDing()
            alarm.dataFormat(event_name=img_url, event_type="img download was failed", gameName="null")
        del r

    @staticmethod
    def get_file_md5(filepath):
        """
        获取imgMD5
        :param filepath:
        :return:
        """
        if not os.path.isfile(filepath):
            return
        myhash = hashlib.md5()
        f = open(filepath, "rb")
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
        f.close()
        print(myhash.hexdigest())
        return myhash.hexdigest()

    @staticmethod
    def aHash(img_path):
        """
        均值哈希算法
        :param img_path:
        :return:
        """
        img = cv2.imread(img_path)
        # 缩放为8*8
        img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
        # 转换为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # s为像素和初值为0，hash_str为hash值初值为''
        s = 0
        hash_str = ''
        # 遍历累加求像素和
        for i in range(8):
            for j in range(8):
                s = s + gray[i, j]
        # 求平均灰度
        avg = s / 64
        # 灰度大于平均值为1相反为0生成图片的hash值
        for i in range(8):
            for j in range(8):
                if gray[i, j] > avg:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    @staticmethod
    def dHash(img_path):
        """
        差值感知算法
        :param img_path:
        :return:
        """
        img = cv2.imread(img_path)
        # 缩放8*8
        img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
        # 转换灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hash_str = ''
        # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
        for i in range(8):
            for j in range(8):
                if gray[i, j] > gray[i, j + 1]:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    @staticmethod
    def cmpHash(hash1, hash2):
        """
        Hash值对比
        :param hash1:
        :param hash2:
        :return:
        """
        n = 0
        # hash长度不同则返回-1代表传参出错
        if len(hash1) != len(hash2):
            return -1
        # 遍历判断
        for i in range(len(hash1)):
            # 不相等则n计数+1，n最终为相似度
            if hash1[i] != hash2[i]:
                n = n + 1
        return n


class AlarmDingDing:
    def __init__(self):
        self.DD_WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send?access_token" \
                              "=6e39bad32fa92c037b6efe2ebb182168ccd29494b77d6fb9066c43f01de8dcd9 "
        self.DD_WEBHOOK_URL = "https://oapi.dingtalk.com/robot/send?access_token" \
                              "=812086e97c51839e166c50246bcb990c778514f0e5d01b563094752598623c9c "
        self.headers = {'Content-Type': 'application/json'}
        self.hostname = socket.gethostname()
        print(self.hostname)

    # def get_hostname(self):
    #     hostname = socket.gethostname()
    #     return hostname
    def dataFormat(self, **kwargs):
        alarm_time = time.strftime("%Y-%m-%d %H:%M:%S")
        msg_template = """[{}]-{}
        告警时间：{}
        事件名称：{}
        事件类型：{}
        元素名称：{}
        当前资源：{}
        原始资源：{}
        访问主机：{}
        {}
        {}
                """.format('H5',
                           '告警',
                           alarm_time,
                           kwargs['event_name'],
                           kwargs['event_type'],
                           kwargs['gameName'],
                           kwargs['curr_url'],
                           kwargs['orig_url'],
                           self.hostname,
                           "请关注...",
                           "a-ansible-1定时任务"
                           )
        msg_content = {
            "msgtype": "text",
            "text": {
                "content": msg_template
            },
            "at": {
                "isAtAll": True
            }
        }
        try:
            resp = requests.post(self.DD_WEBHOOK_URL, data=json.dumps(msg_content), headers=self.headers, timeout=2)
            if resp.status_code != 200:
                print(resp.text)
        except Exception as e:
            print(e)
