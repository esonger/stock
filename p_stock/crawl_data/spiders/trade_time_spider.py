# -*- coding: utf-8 -*-

import json
import scrapy
import global_var as gv
from common.spider_base import SpiderBase
from item.trade_time_item import TradeTimeItem, TradeTimeList
from libs.tong_lian import TongLian


class TradeTimeSpider(SpiderBase):
    '''
    获取沪深交易日历
    '''

    name = gv.SPIDER_TRADE_TIME

    def __init__(self):
        self.tong_lian = TongLian()
        super(TradeTimeSpider, self).__init__()

    def start_requests(self):
        yield scrapy.Request(url=self.tong_lian.get_trade_cal(), headers=self.tong_lian.get_auth())

    def parse(self, response):
        if response.status == 200:
            trade_dict = dict()
            trade_time_list = TradeTimeList()
            count = 0
            for item in self.tong_lian.get_data(json.loads(response.body)):
                count += 1
                if trade_dict.get(item['calendarDate']):
                    if item['exchangeCD'] == gv.EXCHANGE_SHANGHAI and item['isOpen']:
                        trade_dict[item['calendarDate']].xshg_open = gv.EXCHANGE_OPNE
                    elif item['exchangeCD'] == gv.EXCHANGE_SHENZHEN and item['isOpen']:
                        trade_dict[item['calendarDate']].xshe_open = gv.EXCHANGE_OPNE
                else:
                    trade_item = TradeTimeItem(_id=item['calendarDate'], weekend=item['isWeekEnd'],
                                               month_end=item['isMonthEnd'], quarter_end=item['isQuarterEnd'],
                                               year_end=item['isYearEnd'])
                    if item['exchangeCD'] == gv.EXCHANGE_SHANGHAI and item['isOpen']:
                        trade_item.xshg_open = gv.EXCHANGE_OPNE
                    elif item['exchangeCD'] == gv.EXCHANGE_SHENZHEN and item['isOpen']:
                        trade_item.xshe_open = gv.EXCHANGE_OPNE
                    trade_dict[item['calendarDate']] = trade_item
            print 'trade_dict values len', len(trade_dict.values())
            print 'count:', count
            trade_time_list.trade_time_list = trade_dict.values()
            return trade_time_list.dict
