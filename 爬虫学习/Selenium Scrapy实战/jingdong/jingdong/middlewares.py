# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException

class JdSeleniumMiddleware(object):
    # 初始化selenium中间件需要的参数
    # 对于第一个给于默认参数的变量，其后面要么没有变量，如果有则都必须给默认参数，
    def __init__(self,headless,load_img,timeout=None):
        # 设置无界面选项,默认是无界面
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        # 设置不加载图片
        if not load_img:
            prefs = {"profile.managed_default_content_settings.images":2}
            chrome_options.add_experimental_option("prefs",prefs)
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # 设置超时时间
        self.timeout = timeout
        self.browser.set_page_load_timeout(self.timeout)
        # 设置等待时间
        self.wait = WebDriverWait(self.browser,self.timeout)

    # 从settings中注入信息（依赖注入）
    @classmethod
    def from_crawler(cls, crawler):
        # get可以用来设置如果没有从settings中获取到值，则给一个默认值
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),headless=crawler.settings.get('HEADLESS',True),load_img=crawler.settings.get('LOAD_IMG',False))

    def __del__(self):
        '''析构函数'''
        self.browser.close()

    def process_request(self, request, spider):
        '''使用selenium来实现京东商品页面动态渲染后的html页面获取'''
        page = request.meta.get('page')
        try:
            # 在浏览器中打开url
            self.browser.get(request.url)
            # 多页处理
            if page > 1:
                # 等待input输入框加载成功
                inputbar = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#page_jump_num')))
                # 等待确定按钮加载成功
                button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_bottomPage .p-skip > a.btn.btn-default')))
                # 修改页码
                inputbar.clear()
                inputbar.send_keys(page)
                # 点击确定
                button.click()
            # 等待数据加载完成
            # 判断跳转框的value是否包含page值
            self.wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,'#page_jump_num'),str(page)))
            # 判断p-price这个元素是否被放入Dom中
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#plist .gl-item .p-price')))
            # 返回一个html页面的响应
            #print(self.browser.page_source)
            return HtmlResponse(url=request.url,body=self.browser.page_source,request=request,encoding='utf-8',status=200)
        # 处理超时异常
        except TimeoutException:
            return HtmlResponse(url=request.url,status=500,request=request)
