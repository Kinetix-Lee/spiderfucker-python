#!/usr/bin/python3
# coding=utf-8

import json, os
from utils.parse import Parse

class ConvertToJson:
  def convert(self, fileSource, fileSource_output):
    parse = Parse()
    parsed = parse.ParseFile(fileSource)
    result = {
      'alloweds': parse.GetAlloweds(parsed),
      'blockeds': parse.GetBlockeds(parsed),
      'neutrals': parse.GetNeutrals(parsed),
    }
    json.dump(result, fileSource_output, sort_keys=True, indent=2)
