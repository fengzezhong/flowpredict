from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()


def auto_buy(username, password):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "打开登陆界面")

    # https://www.vmall.com/product/10086250925335.html
    # https://www.vmall.com/product/10086250925335.html?ANONYMITY_LOGIN_NAME=139****9884&ANONYMITY_EMAIL=13984*****%40qq.com&ANONYMITY_LOGIN_MOBILE=139****9884

    driver.get(
        "https://www.vmall.com/product/10086250925335.html?ANONYMITY_LOGIN_NAME=139****9884&ANONYMITY_EMAIL=13984*****%40qq.com&ANONYMITY_LOGIN_MOBILE=139****9884")

    # https://www.vmall.com/product/10086250925335.html?ANONYMITY_LOGIN_NAME=139****9884&ANONYMITY_EMAIL=13984*****%40qq.com&ANONYMITY_LOGIN_MOBILE=139****9884
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "开始填写账号密码")
    driver.find_element_by_id('pro-operation')
    driver.find_element_by_link_text("提前登录").click()

    time.sleep(30)  # 正在登陆

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "登陆成功")
    count = 0
    while True:

        try:
            count += 1
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "开始第 %s 次抢购......" % count)

            # 打开购物车并选中商品
            driver.get(
                "https://www.vmall.com/product/10086250925335.html?ANONYMITY_LOGIN_NAME=139****9884&ANONYMITY_EMAIL=13984*****%40qq.com&ANONYMITY_LOGIN_MOBILE=139****9884")

            # driver.find_element_by_class_name("hwid-input-wrap")
            # driver.find_element_by_class_name("hwid-input hwid-input-pwd").send_keys(password)
            # driver.find_element_by_id("loginsubmit").click()

            driver.find_element_by_id("pro-operation")
            driver.find_element_by_link_text("支付订金").click()

            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "点击提交订单")
            time.sleep(5)  # 提交订单前必须等待几秒【感觉跟电脑性能快慢有关，不卡的电脑可以适当降低尝试】
            # driver.find_element_by_id('order-submit').click()  # 提交订单
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "订单提交成功,请前往订单中心待付款付款")
            print("")
            continue
        except Exception as e:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "抢购出现异常，重新抢购: ", e)

            time.sleep(0.001)
            continue


auto_buy('账号', '密码')
