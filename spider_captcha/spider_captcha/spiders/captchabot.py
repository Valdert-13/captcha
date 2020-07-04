# -*- coding: utf-8 -*-
import scrapy


class CaptchabotSpider(scrapy.Spider):
    name = 'captchabot'
    allowed_domains = ['https://rosreestr.ru/wps/portal/online_request']
    start_urls = ['http://https://rosreestr.ru/wps/portal/online_request/']

    def parse(self, response):
        pass
