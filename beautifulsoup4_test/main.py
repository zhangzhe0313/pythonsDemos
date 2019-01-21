#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: main.py
# @Time: 2019-1-21 14:52

# 主入口
from beautifulsoup4_test.htmldownloader.htmlDownloader import HtmlDownLoad
from beautifulsoup4_test.htmlstrparser.htmlParser import HtmlParser

if __name__ == '__main__':
    __test_url = 'http://www.seputu.com/'

    __htmldown_loader = HtmlDownLoad(__test_url)
    __html_str = __htmldown_loader.downloadHtml()

    __html_parser = HtmlParser(__html_str)
    __parse_result = __html_parser.htmlParserContent()

    print(__parse_result)