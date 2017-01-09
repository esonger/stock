# -*- coding: utf-8 -*-

'''
处理交易日历
'''

import global_var as gv
from biz.db.trade_time_db import TradeTimeDb
from item.trade_time_item import TradeTimeList
from scrapy.exceptions import DropItem

class TradeTimePipe(object):

    def process_item(self, item, spider):
        if spider.name == gv.SPIDER_TRADE_TIME:
            trade_time_list = TradeTimeList.from_dict(item)
            TradeTimeDb().insert_many(trade_time_list.trade_time_list)
            raise DropItem()
        else:
            return item
