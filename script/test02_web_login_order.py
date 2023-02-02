import unittest
from time import sleep
import page


from base import log
from page.page_web_login import PageWebLogin
from page.page_web_order import PageWebOrder
from util import GetDriver,read_json


class TestWebLoginOrder(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver.get_web_driver()
        self.login = PageWebLogin(self.driver)
        self.order = PageWebOrder(self.driver)

    def tearDown(self) -> None:
        sleep(1)
        # self.driver.quit()

    def test01_web_login_order(self):
        try:
            # 登录
            self.login.page_web_login()
            nickname = self.login.page_web_nickname()
            print("登录后的昵称为：", nickname)
            # 发货
            self.order.page_order_go_goods()
            # 打印订单
            order_no = self.order.page_order_get_on()
            print("发货的订单为：", order_no)
            # self.assertIn(page.web_order_on, order_no)
            # self.assertIn(order_no, read_json("expect.json", "expect")[0][0])
            #log.info("=======>发货成功，发货的订单号为：{}".format(read_json("expect.json", "expect")[0][0]))

        except Exception as e:
            log.error(e)
            # 截图
            self.order.base_get_img()
            # 抛异常
            raise