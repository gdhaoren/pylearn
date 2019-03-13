	# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
	name = 'login'
	allowed_domains = ['www.renren.com']
	#start_urls = ['http://www.renren.com/']

	# post提交执行登陆
	def start_requests(self):
		# 提交地址
		url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019222239522'
		# 添加post表单信息
		data = {
				'email':'744794581@qq.com',
				'icode':'',
				'origURL':'http://www.renren.com/home',
				'domain':'renren.com',
				'key_id':'1',
				'captcha_type':'web_login',
				'password':'578ab27848919b835468763627e2954154f8a3cdf85e487e2e10ced51cbeca5c',
				'rkey':'de60e626a17db954ad57038248f290e4',
				'f':'http%3A%2F%2Fwww.renren.com%2F313353321%2Fprofile'
			}
		yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse,meta={'cookiejar':True})

	# 获取登录后的cookie并生成新的带有cookie的请求，进而访问登录后的主页，状态维持
	def parse(self, response):
		print("登陆中......")
		print('登录成功，登陆后的cookie为：')
		print(response.headers.getlist('Set-Cookie'))
		# 返回一个新的登录链接 继续登录获取页面信息
		yield scrapy.Request(url='http://www.renren.com/313353321',callback=self.parseHomepage,meta={'cookiejar':True})

	def parseHomepage(self,response):
		# 带着cookie请求访问主页
		print(f'主页title：{response.css("title::text").extract_first()}')




        
