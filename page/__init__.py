from selenium.webdriver.common.by import By
import config

"""
    一、web后台登录配置信息整理
"""
# 用户名
web_login_username = By.CSS_SELECTOR, "[name='username']"
# 密码
web_login_pwd = By.CSS_SELECTOR, "[name='password']"
# 验证码
web_login_verify = By.CSS_SELECTOR, "[name='vertify']"
# 登录按钮
web_login_submit = By.CSS_SELECTOR, "[name='submit']"
# 昵称
web_login_nickname = By.CSS_SELECTOR, ".bgdopa-t"
"""
    二、web发货配置信息整理
"""
# 订单菜单
web_order = By.XPATH, "//a[text()='订单']"
# 左侧菜单 发货单
web_order_goods = By.XPATH, "//a[text()='发货单']"
# iframe
web_order_iframe = By.CSS_SELECTOR, "#workspace"
# 去发货 //div[text()='202112161517008312']/../..//td[@class='handle']//a[1]
web_order_go_goods = By.XPATH, "//a[text()='去发货']"


# 物流公司
web_order_company = By.CSS_SELECTOR, "[value='YZPY']"
# 配送单号
web_order_order_no = By.CSS_SELECTOR, "#invoice_no"
# 确认发货
web_order_goods_ok = By.CSS_SELECTOR, ".ncap-btn-send"
# 打印配置单
web_order_print_order = By.CSS_SELECTOR, ".fa-print"
# 获取订单编号
web_order_on = By.XPATH, "//div[@id='printDiv']/div[@class='contact-info']/dl[1]/dd[2]"