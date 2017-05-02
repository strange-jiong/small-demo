#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-23 23:22:09
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

__doc__ = """Usage:
  quick_example.py tcp <host> <port> [--timeout=<seconds>]
  quick_example.py serial <port> [--baud=9600] [--timeout=<seconds>]
  quick_example.py -h | --help | --version
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__,help=True, version='0.1.1rc')
    print arguments

    # print arguments['host']
