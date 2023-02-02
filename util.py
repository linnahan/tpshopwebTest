import os, json
from selenium import webdriver
import logging.handlers
from config import DIR_PATH, HOST


class GetDriver:

    __web_driver = None
    # 获取Web Driver
    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get(HOST)
            cls.driver.maximize_window()
        return cls.driver

# 日志封装
class GetLog:
    __log = None
    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = DIR_PATH + os.sep + "log" + os.sep + "tpshop_auto.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log

    # 读取json工具
def read_json(filename, key):
    file_path = DIR_PATH + os.sep + "data" + os.sep + filename
    arrs = []
    with open(file_path, "r", encoding="utf-8") as f:
        for data in json.load(f).get(key):
            arrs.append(tuple(data.values())[1:])
        return arrs

if __name__ == '__main__':
    GetLog.get_log().info("日志测试")
    print(read_json("expect.json", "expect"))

