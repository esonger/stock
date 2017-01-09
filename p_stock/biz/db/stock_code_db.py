# -*- coding: utf-8 -*-

from common.db_base import DBBase
from item.stock_code_item import StockCodeItem


class StockCodeDb(DBBase):
    '''
    交易时间的数据库操作
    '''

    table = 'stock_code'

    def __init__(self):
        super(StockCodeDb, self).__init__()
        self.obj_cls = StockCodeItem


if __name__ == '__main__':
    pass