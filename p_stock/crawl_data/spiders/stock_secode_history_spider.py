# -*- coding: utf-8 -*-

import urlparse
import scrapy
import xlrd
import global_var as gv
from common.spider_base import SpiderBase
from item.stock_second_item import StockSecondItem

class StockCodeSpider(SpiderBase):
    '''
    股票历史分笔
    '''

    name = gv.SPIDER_STOCK_CODE

    shgz_host = 'query.sse.com.cn'
    shez_host = 'www.szse.cn'
    start_urls = [
        'http://query.sse.com.cn/security/stock/downloadStockListFile.do?csrcCode=&stockCode=&areaName=&stockType=1',
        'http://www.szse.cn/szseWeb/ShowReport.szse?SHOWTYPE=xlsx&CATALOGID=1110&tab1PAGENUM=1&ENCODE=1&TABKEY=tab1'
    ]

    def make_requests_from_url(self, url):
        url_parse = urlparse.urlparse(url)
        if self.shgz_host == url_parse.hostname:
            headers = dict(
                Referer='http://www.sse.com.cn/assortment/stock/list/share/'
            )
            return scrapy.Request(url, headers=headers, callback=self.parse_shgz)
        elif self.shez_host == url_parse.hostname:
            return scrapy.Request(url, callback=self.parse_shez)
