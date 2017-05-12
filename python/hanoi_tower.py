#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-12 15:22:45
# @Author  : jiong (447991103@qq.com)
# @Link    : ${link}
# @Version : $Id$

import os
count = 1
def test(num, src, dst, rest):
    global count

    if num < 1:
        print False
    elif num == 1:
        print "%d:\t%s -> %s" % (count, src, dst)
        count += 1
    elif num > 1:
        test(num - 1, src, rest, dst)
        test(1, src, dst, rest)
        test(num - 1, rest, dst, src)


test(3, 'A', 'C', 'B')