# -*- coding: utf-8 -*-

import global_var as gv
from common.item_base import ItemBase

class TradeTimeItem(ItemBase):
    '''
    沪深交易日历
    '''
    def init(self, **kwargs):
        self._id = ''   # 日期 '2016-12-22'
        self.xshg_open = gv.EXCHANGE_CLOSE    # 沪市是否开放 0/1
        self.xshe_open = gv.EXCHANGE_CLOSE    # 深市是否开放 0/1
        self.weekend = gv.EXCHANGE_NO_END     # 是否周末 0/1
        self.month_end = gv.EXCHANGE_NO_END    # 是否月末 0/1
        self.quarter_end = gv.EXCHANGE_NO_END   # 是否季末 0/1
        self.year_end = gv.EXCHANGE_NO_END    # 是否年末 0/1

class TradeTimeList(ItemBase):
    '''
    沪深交易日历 列表
    '''

    def init(self, **kwargs):
        self.trade_time_list = list()
