#!/usr/bin/python3
# coding=utf-8

import re

class Parse:
  def ParseLine(self, line):

    line = re.sub(r'\n', '', line)
    
    if len(line) == 0 or line[0] == '#':
      return None

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
  
  def ParseFile(self, file):
    rules = []
    lines = file.readlines()
    for line in lines:
      parsed = self.ParseLine(line)
      if (parsed != None):
        rules.append(parsed)
    return rules
  
  def GetAlloweds(self, rules):
    output = []
    for rule in rules:
      if rule['strategy'] == True:
        output.append(rule['spider'])
    return output
  
  def GetBlockeds(self, rules):
    output = []
    for rule in rules:
      if rule['strategy'] == False:
        output.append(rule['spider'])
    return output
  
  def GetNeutrals(self, rules):
    output = []
    for rule in rules:
      if rule['strategy'] == None:
        output.append(rule['spider'])
    return output

  def GenerateAlloweds(self, rules):
    output = 'User-agent:'
    for spider in self.GetAlloweds(rules):
      output += spider
    output = output[:-1] + '\nAllow:/'
    return output

  def GenerateBlockeds(self, rules):
    output = 'User-agent:'
    for spider in self.GetBlockeds(rules):
      output += spider
    output = output[:-1] + '\nDisallow:/'
    return output
