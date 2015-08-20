# coding=utf-8 ##以utf-8编码储存中文字符
import re

with open('city.sql') as fr:
	with open('city.txt', 'w+') as fw:
		lines = (line for line in fr if 'INSERT' in line)
		for line in lines:
			ps = re.compile(r'\((.*)\)')
			sl = ps.search(line).groups()[0]
			strs = [str.strip().replace("'",'') for str in sl.split(',')]
			fw.write(strs[1] + ' ' + strs[3] + "\n")
		print "done!"
