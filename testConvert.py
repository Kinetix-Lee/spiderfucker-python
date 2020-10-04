# coding=utf-8

import os
from utils.convertToJson import ConvertToJson

convert = ConvertToJson()

fileSource = open('./config/rules/source.txt', 'r')
fileSource_output = open('./config/rules/source.json', 'w')

convert.convert(fileSource, fileSource_output)

fileSource.close()
fileSource_output.close()
