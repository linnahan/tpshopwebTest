import page
from base.base import Base


class PageWebLogin(Base):
    # 1、输入用户名
    def page_web_username(self, value):
        self.base_input(page.web_login_username,value)

    # 2、输入密码
    def page_web_pwd(self,value):
        self.base_input(page.web_login_pwd, value)

    # 3、输入验证码
    def page_web_verify_code(self,value):
        self.base_input(page.web_login_verify, value)

    # 4、点击登录按钮
    def page_web_login_btn(self):
        self.base_click(page.web_login_submit)

    # 5、获取登录昵称
    def page_web_nickname(self):
        return self.base_get_text(page.web_login_nickname)

    # 登录业务方法
    def page_web_login(self,username="admin",pwd="123456",code="8888"):
        self.page_web_username(username)
        self.page_web_pwd(pwd)
        self.page_web_verify_code(code)
        self.page_web_login_btn()

