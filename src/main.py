#!/usr/bin/python3
# coding=utf-8

import os
from utils.parse import Parse

parse = Parse()

rules = None

with open('../config/rules/source.txt', 'r') as fileSource:
  rules = parse.ParseFile(fileSource)

resultSet = {
  'alloweds': parse.GenerateAlloweds(rules),
  'blockeds': parse.GenerateBlockeds(rules),
}

with open('../output/robots-allowed.txt', 'w') as fileRobotsAllowed:
  fileRobotsAllowed.write(resultSet['alloweds'])
with open('../output/robots-blocked.txt', 'w') as fileRobotsBlocked:
  fileRobotsBlocked.write(resultSet['blockeds'])
with open('../output/robots.txt', 'w') as fileRobots:
  fileRobots.write(resultSet['alloweds'] + '\n' + resultSet['blockeds'])
