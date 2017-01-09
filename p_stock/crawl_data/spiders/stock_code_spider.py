# -*- coding: utf-8 -*-

import urlparse
import scrapy
import xlrd
import global_var as gv
from common.spider_base import SpiderBase
from item.stock_code_item import StockCodeItem, StockCodeListItem

class StockCodeSpider(SpiderBase):
    '''
    股票code列表,包括上证/深圳 A股
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

    def parse_shgz(self, rs):
        if rs.status == 200:
            body = rs.body.decode('gb2312').replace(' ', '').split('\t\n')
            stock_code_list = StockCodeListItem()
            for item in body[1:]:
                if not item:
                    continue
                item = item.split('\t')
                stock_code = StockCodeItem()
                stock_code._id = item[2]
                stock_code.exchage = gv.EXCHANGE_SHANGHAI
                stock_code.name = item[3]
                stock_code.total_stock = int(float(item[5])*10000)   # 获取单位为万股. *10000, 恢复单位为个
                stock_code.circulate_stock = int(float(item[6])*10000)
                stock_code.up_time = item[4]
                stock_code_list.stock_code_list.append(stock_code)
            yield stock_code_list.dict

    def parse_shez(self, rs):
        if rs.status == 200:
            work_book = xlrd.open_workbook(file_contents=rs.body)
            sheet = work_book.sheet_by_index(0)
            stock_code_list = StockCodeListItem()
            for row in xrange(1, sheet.nrows):
                stock_code = StockCodeItem()
                stock_code._id = sheet.cell_value(row, 5)
                stock_code.exchage = gv.EXCHANGE_SHENZHEN
                stock_code.name = sheet.cell_value(row, 6)
                stock_code.total_stock = int(sheet.cell_value(row, 8).replace(',', ''))
                stock_code.circulate_stock = int(sheet.cell_value(row, 9).replace(',', ''))
                stock_code.up_time = sheet.cell_value(row, 7)
                stock_code_list.stock_code_list.append(stock_code)
            yield stock_code_list.dict

