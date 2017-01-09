# -*- coding: utf-8 -*-

import traceback
from common import connector


class DBBase(object):

    __limit = 30    # 查询默认限制

    def __init__(self):
        self.db = connector.MongoCon.get_database()

    @property
    def col(self):
        return self.db[self.table]

    def insert_one(self, obj):
        try:
            obj = self.get_obj(obj)
            self.col.insert_one(obj)
        except:
            self.error()

    def insert_many(self, objs):
        try:
            insert_list = list()
            for obj in objs:
                obj = self.get_obj(obj)
                insert_list.append(obj)
                if len(insert_list) == 1000:
                    self.col.insert_many(insert_list)
                    insert_list = list()
            if insert_list:
                self.col.insert(insert_list)
        except:
            self.error()

    def replace_one(self, filter_, obj, *args, **kwargs):
        '''
        如果filter_ 匹配存在则用replacement 替换, 否则插入
        :param filter_:
        :param replacement:
        :param args:
        :param kwargs:
        :return:
        '''
        try:
            obj = self.get_obj(obj)
            self.col.replace_one(filter_, obj, upsert=True)
        except:
            self.error()

    def replace_many(self, objs):
        try:
            for obj in objs:
                self.replace_one({'_id': obj._id}, obj)
        except:
            self.error()

    def get_obj(self, obj):
        '''
        如果是self.obj_cls对象则返回, obj的字典表示
        :param obj:
        :return:
        '''
        if isinstance(obj, self.obj_cls):
            return obj.dict
        return obj

    def error(self, msg=''):
        print traceback.format_exc()

