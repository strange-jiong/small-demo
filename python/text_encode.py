#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-13 16:46:54
# @Author  : jiong (447991103@qq.com)
# @Version : $Id$

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re

s = 'html =  111 , body    = big'
secret = '10'


def encode(s, secret):
	# i.span() 记录了字符串的位置下标
	string = list(s)

	index = []
	for i in re.finditer(r'\s*=\s*', s):
		# print i.group(), i.span()
		index.append(i.span())

	a = 0
	for each in secret:
		if each == '1':
			index = []
			for i in re.finditer(r'\s*=\s*', s):
				# print i.group(),i.span()
				index.append(i.span())
				# print 'a',a
				# print index[a][0],index[a][1]
			# 替换完' ='或者'= '对原始字符串和字符数组进行更新
			string[index[a][0]:index[a][1]] = ' ='
			s = ''.join(string)
			string = list(s)
		else:
			index = []
			for i in re.finditer(r'\s*=\s*', s):
				# print i.group(),i.span()
				index.append(i.span())
			string[index[a][0]:index[a][1]] = '= '
			s = ''.join(string)
			string = list(s)
		a += 1
	print 'encode result:', ''.join(string)
	return ''.join(string)


def decode(s):
	res = []
	for i in re.finditer(r'\s*=\s*', s):
		if i.group() == ' =':
			res.append('1')
		else:
			res.append('0')
	print 'decode result:', ''.join(res)
	return ''.join(res)

	# print s
if __name__ == '__main__':
	print 'original data:', s
	print 'cipher text:',secret
	s = encode(s, secret)
	decode(s)
