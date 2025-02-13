from selenium import webdriver
from nmu.common.CheckSystem import CheckSystem
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

class Browser(object):
    def __init__(self, chrome_location=None, isHeadless=False):
        self.chrome_location = chrome_location
        # 设置 ChromeOptions
        chrome_options = Options()

        # 启用无头模式（如果需要）
        if isHeadless:
            chrome_options.add_argument("--headless")

        # 禁用增强型保护
        chrome_options.add_argument("--disable-features=RendererCodeIntegrity")
        chrome_options.add_argument("--disable-site-isolation-trials")
        chrome_options.add_argument("--no-sandbox")  # 允许 root 用户运行
        chrome_options.add_argument("--disable-dev-shm-usage")  # 避免 `/dev/shm` 共享内存问题
        chrome_options.add_argument("--remote-debugging-port=9222")  # 远程调试端口
        chrome_options.add_argument("--disable-gpu")  # 禁用 GPU
        chrome_options.add_argument("--disable-software-rasterizer")  # 禁用软件渲染

        # 禁用证书错误
        chrome_options.add_argument("--ignore-certificate-errors")

        chrome_options.add_experimental_option('detach', True)

        # 获取 chromedriver 的绝对路径（确保路径正确）
        if self.chrome_location is None:
            chrome_options.binary_location = CheckSystem.get_chrome_path()  # 设置浏览器路径
        else:
            chrome_options.binary_location = self.chrome_location  # 设置浏览器路径
        chromedriver_path = CheckSystem.get_dirver_path()


        # 检查路径是否有效
        if not os.path.exists(chromedriver_path):
            raise ValueError(f"The chromedriver path is invalid: {chromedriver_path}")

        # 使用 Service 类指定 chromedriver 路径
        service = Service(chromedriver_path)

        # 使用指定的 chromedriver 路径初始化浏览器
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_driver(self):
        return self.driver

    def close_browser(self):
        self.driver.quit()