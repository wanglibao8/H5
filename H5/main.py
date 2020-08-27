# coding=utf-8
import datetime
import os
import shutil
import time

import Action


def img_collect(wzry, img_section):
    """
    收集幸运折扣中设计的img
    :param img_section:
    :param wzry:
    :return:
    """
    config = Action.config
    action_version = config.getConfig("H5.conf", "version", "wzry_version")
    wzry_version = config.getConfig("version/version.conf", "version", "wzry_version")
    ImgCheck = Action.ImgCheck
    options_list = config.getOptions(img_section)
    for i in options_list:
        if "action" in i:
            action = config.getConfig("H5.conf", img_section, i)
            try:
                wzry.click(action)
            except Exception as e:
                print(e)
                wzry.quit()
                exit()
        elif "close" in i:
            action = config.getConfig("H5.conf", img_section, i)
            try:
                wzry.click(action)
            except Exception as e:
                print(e)
                wzry.quit()
                exit()
        else:
            print(i)
            element_img = config.getConfig("H5.conf", img_section, i)
            try:
                img_url = wzry.collect_img(element_img)
                print(img_url)
                filename = os.path.basename(img_url)
                print(filename)
                ImgCheck.download_img(img_url, "current_img/", filename)
                if action_version != wzry_version:
                    ImgCheck.download_img(img_url, "original_img/", filename)
            except Exception as e:
                print(e)
                wzry.screenshot("error_img/", i)
                alarm = Action.AlarmDingDing()
                alarm.dataFormat(event_name="H5_WZRY", event_type="元素不存在", gameName=element_img,
                                 curr_url="http://39.106.183.113"
                                          "/H5/error_img/" + i + '.png',
                                 orig_url=".....")


def wzry_actions(config, wzry, section, path):
    """
    点击客服，提交意见，时长兑换
    :param path:
    :param config:
    :param section:
    :param wzry:
    :return:
    """

    options_list = config.getOptions(section)
    for i in options_list:
        actions = config.getConfig("H5.conf", section, i)
        if i == "send_keys":
            wzry.send_comments(actions, "测试！！！")
        elif "onback" in i:
            try:
                wzry.click(actions)
            except Exception as e:
                print(e)
                wzry.quit()
                exit()
        elif "close" in i:
            try:
                wzry.click(actions)
            except Exception as e:
                print(e)
                # wzry.quit()
                # exit()
        else:
            print(i)
            filename = section + "_" + i
            print(filename)
            try:
                wzry.click(actions)
                wzry.screenshot(path, filename)
                # wzry.screebshot_ele(actions, path, i)
            except Exception as e:
                wzry.screenshot("error_img/", filename)
                alarm = Action.AlarmDingDing()
                alarm.dataFormat(event_name="H5_WZRY", event_type="元素不存在", gameName=actions,
                                 curr_url="http://39.106.183.113"
                                          "/H5/error_img/" + filename + '.png',
                                 orig_url="http://39.106.183.113"
                                          "/H5/original_img/" + filename + '.png')
                print(e)
                wzry.quit()
                exit()


def wzry_screen_page(sections, path, url, H5_PAGE=None):
    """
    元素截图
    :param num: 重试次数
    :param wzry:
    :param sections:
    :param path:
    :return:
    """
    global i, actions, wzry
    config = Action.config
    action_version = config.getConfig("H5.conf", "version", "wzry_version")
    wzry_version = config.getConfig("version/version.conf", "version", "wzry_version")
    for section in sections:
        options_list = config.getOptions(section)
        # options_list_click = config.getOptions(section + '_click')
        count = 0
        while count <= 5:
            try:
                wzry = Action.H5Check(url)
                for i in options_list:
                    actions = config.getConfig("H5.conf", section, i)
                    print(i)
                    print(actions)
                    if "close" in i:
                        wzry.click(actions)
                        time.sleep(1)
                    elif "action" in i:
                        wzry.click(actions)
                        time.sleep(5)
                    else:
                        wzry.screebshot_ele(actions, path[0], i)
                        if action_version != wzry_version:
                            wzry.screebshot_ele(actions, path[1], i)
                wzry.quit()
                break
            except Exception as e:
                if count == 5:
                    wzry.screenshot("error_img/", i)
                    alarm = Action.AlarmDingDing()
                    print("alarm.....")
                    if "action" in i or "close" in i:
                        alarm.dataFormat(event_name=H5_PAGE, event_type="元素不存在", gameName=actions,
                                         curr_url="http://39.106.183.113"
                                                  "/H5/error_img/" + i + '.png',
                                         orig_url="页面按钮{}不存在。".format(i))
                    else:
                        alarm.dataFormat(event_name=H5_PAGE, event_type="元素不存在", gameName=actions,
                                         curr_url="http://39.106.183.113"
                                                  "/H5/error_img/" + i + '.png',
                                         orig_url="http://39.106.183.113"
                                                  "/H5/original_img/" + i + '.png')
                count += 1
                print(e)
                wzry.quit()





def page_main(url, pages, H5_PAGE="H5_WZRY"):
    wzry_screen_page( pages, ["current_img/", "original_img/"], url, H5_PAGE)


def get_filelist(dir, ImgCheck):
    """
    根据img存储目录计算img hash
    :param dir:
    :param ImgCheck:
    :return:
    """
    for home, dirs, files in os.walk(dir):
        # print("#######dir list#######")
        # for dir in dirs:
        #     print(dir)
        # print("#######dir list#######")
        dHash = {}
        aHash = {}
        # print("#######file list#######")
        for filename in files:
            # print(filename)
            fullname = os.path.join(home, filename)
            # print(fullname)
            ahash_str = ImgCheck.aHash(fullname)
            aHash[filename] = ahash_str
            dhash_str = ImgCheck.dHash(fullname)
            dHash[filename] = dhash_str
        # print("#######file list#######")
        return aHash, dHash

def copy_file(source, filename):
    hash_dir = "hash_img/"+filename
    shutil.copy(source, hash_dir)



def action_main(section, url):
    wzry_page = Action.H5Check(url)
    config = Action.config
    action_version = config.getConfig("H5.conf", "version", "wzry_version")
    wzry_version = config.getConfig("version/version.conf", "version", "wzry_version")
    if action_version == wzry_version:
        wzry_page.screenshot("current_img/", "home_page")
        wzry_actions(config, wzry_page, section, "current_img/")
    else:
        wzry_page.screenshot("original_img/", "home_page")
        wzry_actions(config, wzry_page, section, "original_img/")
    wzry_page.quit()
    return action_version


def image_main(sections, url):
    for section in sections:
        wzry_page = Action.H5Check(url)
        img_collect(wzry_page, section)
        wzry_page.quit()


def img_check():
    ImgCheck = Action.ImgCheck
    hash_1, hash_3 = get_filelist("current_img/", ImgCheck)
    hash_2, hash_4 = get_filelist("original_img/", ImgCheck)
    alarm = Action.AlarmDingDing()
    for k in hash_1:
        try:
            a1, a2 = hash_1[k], hash_3[k]
            b1, b2 = hash_2[k], hash_4[k]
            c1 = ImgCheck.cmpHash(a1, b1)
            c2 = ImgCheck.cmpHash(a2, b2)
            print(c1, c2)
            print(k)
            if c1 >= 10:
                tag = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
                copy_file("current_img/"+k, tag+k)
                alarm.dataFormat(event_name="H5", event_type="img 差值校验", gameName=k,
                                 curr_url="http://39.106.183.113/H5/hash_img/" + tag+k, orig_url="http://39.106.183.113"
                                                                                                "/H5/original_img/" + k)
            if c2 >= 10:
                tag = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
                copy_file("current_img/"+k, tag+k)
                alarm.dataFormat(event_name="H5", event_type="img  方差校验", gameName=k,
                                 curr_url="http://39.106.183.113/H5/hash_img/" + tag+k, orig_url="http://39.106.183.113"
                                                                                                "/H5/original_img/" + k)
        except:
            pass


if __name__ == '__main__':
    wZry_url = "http://xunyou.mobi/payments/?oid=2AF283A658C46B19B2215F5D6338890&aid=1104466820&uid=328173424&us=3&ed" \
               "=2017-12-19%2000%3A38%3A28&n=1&mp=1&go=7&ms=1&pt=0&sv=3.9.4.13&md=PCT-AL10&ad=-1&sd=-1&lv=1.0&algorithm=v2" \
               "&version=3.3.9a&timestamp=1590571130&appid=1104466820&openid=29AF283A658C46B19B2215F5D6338890&sig" \
               "=10cf84c8efcec4dee9054c8588d14075&encode=2&msdkEncodeParam" \
               "=67C0BD71794562E1860C1BCE31B5D3D05CD302ABCF03A386B99974B2737E51D822299A721AA859AB3BB3F0A6EC085B25D64A9977CC3CFF4A3D85DB1892446155804D22737E2208F83A76976B0CFF51440AB519F4A1EA7399F5F93C5E4542552138450A83073958804617617B7D78D6A81DEDB0DB7BE1200FC9465F382173802E7B2C3D56D6516531E8E18D8142E07BB0F07E1CD852AF8B2E0D89C47EA15443104D08B9AA04C62C51E87C6FF4C3B18F96 "

    wZry_url_B = "http://xunyou.mobi/payments/?oid=811a554fd201&aid=1&uid=936587859&us=4&ed=2020-10-29%2014%3A28%3A27" \
                 "&n%22%20\%20%22=1&mp=1&go=0&ms=1&pt=1&sv=3.9.7.1&md=PCT-AL10&ad=-1&sd=-1&lv=1.0&algorithm=v2" \
                 "&version=2.16.0a%22%20\%20%22&timestamp=1595410092733&msdkEncodeParam" \
                 "=EDE4B44F5082DC96B089407342B73339 "

    hPjy_url = "https://pay.xunyou.mobi/D3E91652-4169-42E3-829F-1D82EFBA2147/?user_openid=811a554fd201&token=a8a2" \
               "-3b37ce01918b&app_id=1&user_id=936587859&user_status=4&expired_date=2020-10-29%2014%3A28%3A27&guid" \
               "=D3E91652-4169-42E3-829F-1D82EFBA2147&network=1&mpath=1&go=0&mobile_switch=1&pt=1&sv=3.9.7.1&md=PCT" \
               "-AL10&algorithm=v2&version=2.16.0a&timestamp=1595409885691&msdkEncodeParam" \
               "=5994787356EFC6833A14F773D8580738 "

    cYhx_url = "https://pay.xunyou.mobi/B5EE869C-4BBD-4C86-B90B-4C136440BD5A/?user_openid=811a554fd201&token=a8a2" \
               "-3b37ce01918b&app_id=1&user_id=565861228&user_status=5&expired_date=2020-07-12%2019%3A33%3A59&guid" \
               "=B5EE869C-4BBD-4C86-B90B-4C136440BD5A&network=1&mpath=1&go=0&mobile_switch=1&pt=0&sv=3.9.7.1&md=PCT" \
               "-AL10&algorithm=v2&version=2.16.0a&timestamp=1595589815651&msdkEncodeParam" \
               "=87A872DBA455A53FC6585751E6E05D4C "
    config = Action.config

    # img_check()

    # 收集静态图片
    # sections = ["lucky_discount_window_imgs", "main_page_imgs"]
    # image_main(sections)
    #
    # 页面按钮截图
    # sections = ["onService_actions", "products_actions", "onActivity_actions"]
    # # sections = ["onService_actions"]
    # for section in sections:
    #     action_main(section)

    # 主页面截图
    page_main(wZry_url, ["wZry_page_main"])
    page_main(wZry_url_B, ["wZry_page_main_B"])
    page_main(hPjy_url, ["hPjy_page_main"], H5_PAGE="H5_HPJY")
    page_main(cYhx_url, ["cYhx_page_main"], H5_PAGE="H5_CYHX")



    # 对比初始图片和当前图片相似度
    # img_check()

    # 版本控制
    action_version = config.getConfig("H5.conf", "version", "wzry_version")
    wzry_version = config.getConfig("version/version.conf", "version", "wzry_version")
    if action_version != wzry_version:
        config.setConfig("H5.conf", "version", "wzry_version", wzry_version)
