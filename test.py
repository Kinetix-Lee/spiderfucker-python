#!/usr/bin/python3
# coding=utf-8

import main

def testOpen():
  with open('./output/robots-allowed.txt', 'r') as f:
    return len(f.read()) > 0

assert testOpen()
