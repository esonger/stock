# -*- coding: utf-8 -*-

from common.db_base import DBBase
from item.trade_time_item import TradeTimeItem


class TradeTimeDb(DBBase):
    '''
    交易时间的数据库操作
    '''

    table = 'trade_time'

    def __init__(self):
        super(TradeTimeDb, self).__init__()
        self.obj_cls = TradeTimeItem


if __name__ == '__main__':
    pass