#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: tessseract_demo.py
# @Time: 2019-1-25 10:19

# 识别传统二维码-字母-数字

import pytesseract
from PIL import Image

image = Image.open('test_number.png')
# 设置tesseract的安装路径
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Administrator.SKYUSER-KNVGSHO\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
code = pytesseract.image_to_string(image)

print('code: %s' % code)