# -*- coding: utf-8 -*-

import scrapy
import json

class SpiderBase(scrapy.Spider):

    def parse_jsonp(self, data):
        return self.parse_json(data[data.find('(')+1:data.find(')')])

    def parse_json(self, data):
        return json.loads(data)