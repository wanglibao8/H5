import os
import time
import configparser
from selenium import webdriver


def collect_img():
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    wd = webdriver.Chrome(r'C:\Users\xiaor\Desktop\chromedriver.exe')
    wd.implicitly_wait(10)
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    # wd.get("https://www.baidu.com/")

    # 截图
    # wd.get_screenshot_as_file('1.png')
    wd.get(
        'http://xunyou.mobi/payments/?oid=29AF283A658C46B19B2215F5D6338890&aid=1104466820&uid=328173424&us=3&ed=2017'
        '-12-19%2000%3A38%3A28&n=1&mp=1&go=7&ms=1&pt=0&sv=3.9.4.13&md=PCT-AL10&ad=-1&sd=-1&lv=1.0&algorithm=v2'
        '&version=3.3.9a&timestamp=1590571130&appid=1104466820&openid=29AF283A658C46B19B2215F5D6338890&sig'
        '=10cf84c8efcec4dee9054c8588d14075&encode=2&msdkEncodeParam'
        '=67C0BD71794562E1860C1BCE31B5D3D05CD302ABCF03A386B99974B2737E51D822299A721AA859AB3BB3F0A6EC085B25D64A9977CC3CFF4A3D85DB1892446155804D22737E2208F83A76976B0CFF51440AB519F4A1EA7399F5F93C5E4542552138450A83073958804617617B7D78D6A81DEDB0DB7BE1200FC9465F382173802E7B2C3D56D6516531E8E18D8142E07BB0F07E1CD852AF8B2E0D89C47EA15443104D08B9AA04C62C51E87C6FF4C3B18F96')

    try:
        img_list = ["#lotteryBg", "#body-content > t-notice > div.modal-relative > div > div > current_img.title",
                    "#body-content > t-notice > div.modal-relative > div > div > current_img.card-tips",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item1 > div.card.card-f > current_img:nth-child(1)",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item1 > div.card.card-f > current_img.card-btn",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item1 > div.card.card-r > current_img",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item2 > div.card.card-f > current_img:nth-child(1)",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item2 > div.card.card-f > current_img.card-btn",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item2 > div.card.card-r > current_img",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item3 > div.card.card-f > current_img:nth-child(1)",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item3 > div.card.card-f > current_img.card-btn",
                    "#body-content > t-notice > div.modal-relative > div > div > div.card-box > div.card-item.card-item3 > div.card.card-r > current_img",
                    "#body-content > t-notice > div.modal-relative > div > div > current_img.btn-start.downup.opacity1",
                    "#body-content > t-notice > div.modal-relative > div > div > current_img.btn-hand.downup.opacity1"]
        for i in img_list:
            element = wd.find_element_by_css_selector(i)
            html_choujiang = element.get_attribute("src")
            print(html_choujiang)
        time.sleep(3)
        wd.quit()
    except Exception as e:
        print(e)
        time.sleep(3)
        wd.quit()


def click_key():
    # 创建 WebDriver 对象，指明使用chrome浏览器驱动
    wd = webdriver.Chrome(r'C:\Users\xiaor\Desktop\chromedriver.exe')
    wd.implicitly_wait(10)
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    # wd.get("https://www.baidu.com/")

    # 截图
    # wd.get_screenshot_as_file('1.png')
    wd.get(
        'http://xunyou.mobi/payments/?oid=29AF283A658C46B19B2215F5D6338890&aid=1104466820&uid=328173424&us=3&ed=2017'
        '-12-19%2000%3A38%3A28&n=1&mp=1&go=7&ms=1&pt=0&sv=3.9.4.13&md=PCT-AL10&ad=-1&sd=-1&lv=1.0&algorithm=v2'
        '&version=3.3.9a&timestamp=1590571130&appid=1104466820&openid=29AF283A658C46B19B2215F5D6338890&sig'
        '=10cf84c8efcec4dee9054c8588d14075&encode=2&msdkEncodeParam'
        '=67C0BD71794562E1860C1BCE31B5D3D05CD302ABCF03A386B99974B2737E51D822299A721AA859AB3BB3F0A6EC085B25D64A9977CC3CFF4A3D85DB1892446155804D22737E2208F83A76976B0CFF51440AB519F4A1EA7399F5F93C5E4542552138450A83073958804617617B7D78D6A81DEDB0DB7BE1200FC9465F382173802E7B2C3D56D6516531E8E18D8142E07BB0F07E1CD852AF8B2E0D89C47EA15443104D08B9AA04C62C51E87C6FF4C3B18F96')

    try:
        # 关闭抽奖弹窗
        element = wd.find_element_by_css_selector(
            "#body-content > t-notice > div.modal-relative > div > div > div.lottery-close")
        element.click()
        time.sleep(5)
        # 查看购买历史
        element = wd.find_element_by_css_selector(
            "#toHistory")
        element.click()
        time.sleep(5)
        # 返回
        element = wd.find_element_by_css_selector(
            "#onBack")
        element.click()
        time.sleep(5)
        # 点击月卡产品
        element = wd.find_element_by_css_selector(
            "#selectProductWidthmonth")
        element.click()
        time.sleep(5)
        # 点击季卡产品
        element = wd.find_element_by_css_selector(
            "#selectProductWidthseason")
        element.click()
        time.sleep(5)
        # 点击半年卡产品
        element = wd.find_element_by_css_selector(
            "#selectProductWidthhalfyear")
        element.click()
        time.sleep(5)
        # 抽奖
        element = wd.find_element_by_css_selector(
            "#onActivity")
        element.click()
        time.sleep(5)
        # 点击月卡抽奖
        element = wd.find_element_by_css_selector(
            "#main > div:nth-child(1) > div > div > div.lotterypanel > div.lotteryproducts > div.lotteryproduct.month")
        element.click()
        time.sleep(5)
        # 点击季卡抽奖
        element = wd.find_element_by_css_selector(
            "#main > div:nth-child(1) > div > div > div.lotterypanel > div.lotteryproducts > div.lotteryproduct.season")
        element.click()
        time.sleep(5)
        # 点击半年卡抽奖
        element = wd.find_element_by_css_selector(
            "#main > div:nth-child(1) > div > div > div.lotterypanel > div.lotteryproducts > "
            "div.lotteryproduct.halfyear")
        element.click()
        time.sleep(5)
        # 客服
        element = wd.find_element_by_css_selector(
            "#onService")
        element.click()
        time.sleep(5)
        # 输入意见
        element = wd.find_element_by_css_selector(
            "#main > div:nth-child(2) > div > div > div.feedback-box > div.panel > textarea")
        element.send_keys("测试！！！")
        time.sleep(5)
        wd.quit()
    except Exception as e:
        print(e)
        wd.quit()


def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/H5.conf'
    config.read(path)
    return config.get(section, key)


def getOptions(section):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/H5.conf'
    config.read(path)
    return config.options(section)


class H5Check:
    def __init__(self, h5_url):
        # 创建 WebDriver 对象，指明使用chrome浏览器驱动
        self.wd = webdriver.Chrome(r'C:\Users\xiaor\Desktop\chromedriver.exe')
        self.wd.implicitly_wait(10)
        self.wd.get(h5_url)
        time.sleep(3)

    def quit(self):
        self.wd.quit()

    def click(self, element):
        """
        根据页面元素实现点击页面按钮
        :param element:
        :return:
        """
        try:
            element = self.wd.find_element_by_css_selector(element)
            element.click()
            time.sleep(5)
        except Exception as e:
            print(e)
            self.quit()
            exit()

    def collect_img(self, element):
        """
        根据页面元素提取img url
        :param element:
        :return:
        """
        try:
            img_url = self.wd.find_element_by_css_selector(element).get_attribute("src")
            print(img_url)
            return img_url
        except Exception as e:
            print(e)
            self.quit()
            exit()

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

    def screenshot(self, img_name):
        path = os.path.split(os.path.realpath(__file__))[0] + '/current_img/'
        self.wd.get_screenshot_as_file(path + img_name+'.png')



def img_collect(wzry):
    """收集幸运折扣中设计的img"""
    # ele = getConfig("lucky_discount_window", "window_info")
    # wzry.outerHTML(ele)
    options_list = getOptions("lucky_discount_window_imgs")
    for i in options_list:
        element_img = getConfig("lucky_discount_window_imgs", i)
        wzry.collect_img(element_img)


def onService_actions(wzry):
    """
    点击客服，提交意见，时长兑换
    :param wzry:
    :return:
    """
    options_list = getOptions("onService_actions")
    for i in options_list:
        actions = getConfig("onService_actions", i)
        print(i)
        if i == "send_keys":
            wzry.send_comments(actions, "测试！！！")
        else:
            wzry.click(actions)


def wzry_actions(wzry, section):
    """
    点击客服，提交意见，时长兑换
    :param section:
    :param wzry:
    :return:
    """
    options_list = getOptions(section)
    for i in options_list:
        actions = getConfig(section, i)
        print(i)
        if i == "send_keys":
            wzry.send_comments(actions, "测试！！！")
        else:
            wzry.click(actions)
            wzry.screenshot(i)


if __name__ == '__main__':
    url = "http://xunyou.mobi/payments/?oid=29AF283A658C46B19B2215F5D6338890&aid=1104466820&uid=328173424&us=3&ed" \
          "=2017-12-19%2000%3A38%3A28&n=1&mp=1&go=7&ms=1&pt=0&sv=3.9.4.13&md=PCT-AL10&ad=-1&sd=-1&lv=1.0&algorithm=v2" \
          "&version=3.3.9a&timestamp=1590571130&appid=1104466820&openid=29AF283A658C46B19B2215F5D6338890&sig" \
          "=10cf84c8efcec4dee9054c8588d14075&encode=2&msdkEncodeParam" \
          "=67C0BD71794562E1860C1BCE31B5D3D05CD302ABCF03A386B99974B2737E51D822299A721AA859AB3BB3F0A6EC085B25D64A9977CC3CFF4A3D85DB1892446155804D22737E2208F83A76976B0CFF51440AB519F4A1EA7399F5F93C5E4542552138450A83073958804617617B7D78D6A81DEDB0DB7BE1200FC9465F382173802E7B2C3D56D6516531E8E18D8142E07BB0F07E1CD852AF8B2E0D89C47EA15443104D08B9AA04C62C51E87C6FF4C3B18F96 "
    wzry_page = H5Check(url)
    close_window = getConfig("lucky_discount_window", "close_window")
    # element_img_1 = getConfig("lucky_discount_window","element_img_1")
    # wzry_page.collect_img(element_img_1)
    # onService_actions(wzry_page)
    wzry_actions(wzry_page, "onActivity_actions")
    # img_collect(wzry_page)
    wzry_page.quit()
