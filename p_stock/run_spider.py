# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from twisted.internet import reactor, defer
from crawl_data.spiders import trade_time_spider
from crawl_data.spiders import stock_code_spider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerRunner


def crawl_run():
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        # yield runner.crawl(trade_time_spider.TradeTimeSpider)
        yield runner.crawl(stock_code_spider.StockCodeSpider)
        reactor.stop()

    crawl()
    reactor.run()

def debug_run():
    from scrapy.crawler import CrawlerProcess
    from scrapy.utils.project import get_project_settings
    process = CrawlerProcess(get_project_settings())
    process.crawl('stock_code')
    process.start()

if __name__ == '__main__':
    # crawl_run()
    debug_run()
