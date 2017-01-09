# -*- coding: utf-8 -*-

'''
处理股票代码
'''

import global_var as gv
from item.stock_code_item import StockCodeListItem
from biz.db.stock_code_db import StockCodeDb
from scrapy.exceptions import DropItem

class StockCodePipe(object):

    def process_item(self, item, spider):
        if spider.name == gv.SPIDER_STOCK_CODE:
            stock_list = StockCodeListItem.from_dict(item)
            StockCodeDb().replace_many(stock_list.stock_code_list)
            raise DropItem()
        else:
            return item
