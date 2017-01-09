# -*- coding: utf-8 -*-

import global_var as gv
from common.item_base import ItemBase

class StockCodeItem(ItemBase):
    '''
    沪深交易日历
    '''
    def init(self, **kwargs):
        self._id = ''   # 股票代码
        self.exchage = ''   # 所在交易所
        self.type = gv.EXCHANGE_STOCK_TYPE_A    # A/B股  默认A股
        self.name = ''  # 股票简称
        self.up_time = ''   # 上市时间
        self.total_stock = float()    # 总发行股本   单位万
        self.circulate_stock = float()    # 流通股本    单位万
        self.board = gv.EXCHANGE_BOARD_MAIN  # 所属市场板块
        self.status = gv.EXCHANGE_STOCK_STATUS_NORMAL     # 当前状态, 正常, 停牌等

class StockCodeListItem(ItemBase):

    def init(self, **kwargs):
        self.stock_code_list = list()

