# -*- coding: utf-8 -*-

'''
交易所相关
以 EXCHANGE_ 为前缀
'''

# 上海交易所
EXCHANGE_SHANGHAI = 'XSHG'
# 深圳交易所
EXCHANGE_SHENZHEN = 'XSHE'

# 开市
EXCHANGE_OPNE = 1
# 休市
EXCHANGE_CLOSE = 0

# 市场周期
# 周末, 月末, 年末
EXCHANGE_WEEKEND = EXCHANGE_MONTHEND = EXCHANGE_YEAREND = 1
# 非周末, 月末, 年末
EXCHANGE_NO_END = 0

# A股
EXCHANGE_STOCK_TYPE_A = 1
# B股
EXCHANGE_STOCK_TYPE_B = 2

# 所属板块
# 主板
EXCHANGE_BOARD_MAIN = 1
# 创业板
EXCHANGE_BOARD_GEM = 2
# 中小板
EXCHANGE_BOARD_SMSE = 3


# 股票状态
# 正常交易
EXCHANGE_STOCK_STATUS_NORMAL = 1
# 停牌
EXCHANGE_STOCK_STATUS_STOP = -1

