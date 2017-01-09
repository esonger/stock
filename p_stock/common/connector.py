# -*- coding: utf-8 -*-

from pymongo import MongoClient, ReadPreference
import conf
import redis


class MongoCon(object):
    """mongodb数据库连接单例类"""
    __connection = None
    __database = None

    @classmethod
    def new_connection(cls):
        '''
        新建一个mongodb的连接
        :return:
        '''
        connection = None
        try:
            connection = MongoClient(",".join(conf.DB_REPLICA_SET),
                                     replicaSet=conf.DB_REPLICA_SET_NAME,
                                     read_preference=ReadPreference.SECONDARY_PREFERRED)
        except Exception, e:
            print e
            connection = MongoClient(host=conf.DB_HOST, port=conf.DB_PORT)
        return connection

    @classmethod
    def get_connection(cls):
        """返回全局的数据库连接
        return mongodb connection
        """
        if cls.__connection is None:
            cls.__connection = cls.new_connection()
        return cls.__connection

    @classmethod
    def new_database(cls):
        '''
        返回一个新的数据库实例
        :return:
        '''
        return cls.new_connection()[conf.DB_NAME]

    @classmethod
    def get_database(cls):
        """返回当前数据库
        return mongodb database
        """
        if cls.__database is None:
            cls.__database = MongoCon.get_connection()[conf.DB_NAME]
        return cls.__database


class RedisCon(object):
    """redis连接单例类"""
    _redis = None

    @classmethod
    def get_connection(cls):
        """返回redis 连接池
        return redis connection pool
        """
        if cls._redis is None:
            cls._redis = redis.StrictRedis(connection_pool=redis.ConnectionPool(host=conf.REDIS_HOST,
                                                                                port=conf.REDIS_PORT,
                                                                                db=conf.REDIS_DB))
        return cls._redis