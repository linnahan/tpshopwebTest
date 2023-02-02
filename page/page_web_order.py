from selenium.webdriver.common.by import By
import page
import  time
from base.base import Base



class PageWebOrder(Base):
    # 订单菜单
    def page_web_order_menu(self):
        self.base_click(page.web_order)

    # 左侧 发货单
    def page_web_order_goods(self):
        self.base_click(page.web_order_goods)

    # 工作区域 去发货
    def page_web_go_goods(self):
        # 切换iframe
        self.base_switch_frame(page.web_order_iframe)
        self.base_click(page.web_order_go_goods)

    # 物流公司
    def page_order_company(self):
        self.base_click(page.web_order_company)

    # 配送单号
    def page_order_input_order_no(self):
        value = str(time.strftime("%Y%m%d%H%M%S"))
        self.base_input(page.web_order_order_no, value)

    # 确认发货
    def page_order_goods_ok(self):
        self.base_click(page.web_order_goods_ok)

    # 打印配置单
    def page_order_print_order(self):
        self.base_click(page.web_order_print_order)

    # 获取订单编号
    def page_order_get_on(self):
        return self.base_get_text(page.web_order_on)

    # 订单发货业务
    def page_order_go_goods(self):
        self.page_web_order_menu()
        self.page_web_order_goods()
        self.page_web_go_goods()
        self.page_order_company()
        self.page_order_input_order_no()
        self.page_order_goods_ok()
        self.page_order_print_order()
