#!/usr/bin/python3
# coding=utf-8

import os
from utils.parse import Parse

parse = Parse()

fileSource = None

try:
  fileSource = open('../config/rules/source.txt', 'r')
except FileNotFoundError:
  raise

fileRobotsAllowed = open('../output/robots-allowed.txt', 'w')
fileRobotsBlocked = open('../output/robots-blocked.txt', 'w')
fileRobots = open('../output/robots.txt', 'w')

rules = parse.ParseFile(fileSource)

resultSet = {
  'alloweds': parse.GenerateAlloweds(rules),
  'blockeds': parse.GenerateBlockeds(rules),
}

fileRobotsAllowed.write(resultSet['alloweds'])
fileRobotsBlocked.write(resultSet['blockeds'])
fileRobots.write(resultSet['alloweds'] + '\n' + resultSet['blockeds'])
