# -*- coding: utf-8 -*-

'''
db配置
'''

import env

# mongodb setting
DB_HOST = "127.0.0.1"
DB_PORT = 27017
DB_NAME = 'stock'
DB_REPLICA_SET = ["127.0.0.1:27017", "127.0.0.1:27018", "127.0.0.1:27019"]
DB_REPLICA_SET_NAME = "rs0"
