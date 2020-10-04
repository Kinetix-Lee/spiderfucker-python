#!/usr/bin/python3
# coding=utf-8

import os, re

def lineParse(line):

  line = re.sub(r'\n', '', line)
  
  if len(line) == 0 or line[0] == '#':
    return

  rule = {
    'spider': '',
    'strategy': '',
  }

  # line.remove('\n')
  splited = line.split(':')

  if len(splited) == 1:
    rule['spider'] = splited[0]
    rule['strategy'] = None # neutral
  elif len(splited) == 2:
    rule['spider'] = splited[0]
    rule['strategy'] = True if splited[1] == 'a' else False # allowed / blocked
  else:
    raise 'File malformatted! '
  
  return rule

def generateAlloweds(rules):
  output = 'User-agent:'
  for i in range(len(rules)):
    rule = rules[i]
    if rule['strategy'] == True:
      output += rule['spider'] + ','
  output = output[:-1]
  output += '\nAllow:/'
  return output

def generateBlockeds(rules):
  output = 'User-agent:'
  for i in range(len(rules)):
    rule = rules[i]
    if rule['strategy'] == False:
      output += rule['spider'] + ','
  output = output[:-1]
  output += '\nDisallow:/'
  return output

fileRaw = open('./raw.txt', 'r')
fileRobotsAllowed = open('./result/robots-allowed.txt', 'w')
fileRobotsBlocked = open('./result/robots-blocked.txt', 'w')
fileRobots = open('./result/robots.txt', 'w')

rules = []

lines = fileRaw.readlines()
for line in lines:
  parsed = lineParse(line)
  if (parsed != None):
    rules.append(parsed)

resultSet = {
  'alloweds': generateAlloweds(rules),
  'blockeds': generateBlockeds(rules),
}

fileRobotsAllowed.write(resultSet['alloweds'])
fileRobotsBlocked.write(resultSet['blockeds'])
fileRobots.write(resultSet['alloweds'] + '\n' + resultSet['blockeds'])
