# -*- coding: utf-8 -*-

import conf
import global_var as gv


class TongLian(object):
    '''
    通联接口
    '''

    HOST = 'https://api.wmcloud.com/%s'
    APIS = dict(
        get_trade_cal=HOST % 'data/v1/api/master/getTradeCal.json'
    )
    TOKEN = conf.TONG_LIAN_TOKEN
    EXCHANGE_SHANGHAI = gv.EXCHANGE_SHANGHAI
    EXCHANGE_SHENZHEN = gv.EXCHANGE_SHENZHEN

    def get_auth(self):
        return dict(Authorization='Bearer %s' % self.TOKEN)

    def get_trade_cal(self, return_url=True, start_date=''):
        '''
        交易所交易日历
        :param return_url: boolean 返回数据或接口url
        :param start_date: 开始时间
        :return:
        '''
        trade_cal = self.APIS['get_trade_cal'] + '?field=&exchangeCD=%s&beginDate=%s&endDate=' % \
                                                 (self.EXCHANGE_SHANGHAI + ',' + self.EXCHANGE_SHENZHEN, start_date)
        if return_url:
            return trade_cal

    def get_data(self, body):
        '''
        从response的body里返回数据
        :param response:
        :return:
        '''
        if body['retCode'] == 1 and body['retMsg'] == 'Success':
            for item in body['data']:
                yield item


if __name__ == '__main__':
    tong_lian = TongLian()
    print tong_lian.get_trade_cal(start_date='19910703')
