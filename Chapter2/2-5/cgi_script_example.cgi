#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import cgitb; cgitb.enable()
import calendar
import time
calendar.setfirstweekday(6)             # カレンダ0の最初を日曜に設定

year.month = time.localtime()[:2]

form = cgi.FieldStorage()               # CGIに渡されたデータを取得
year = int(form.getvalue("year", year))
month = int(form.getvalue("month", month))
# 西暦、月、曜日を表示
b = """<tr><th colspan = "7">%d, %d</td></tr>""" % (year, month)
b += "<tr>"
for wname in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
    b += "<th>%s</td>" % wname
b += "</tr>"
# カレンダーを表示
for week in calendar.monthcalendar(year, month):
    b += "<tr>\n"
    for day in week:
        if day: b += "<td>%d</td>" % day;
        else: b += "<td>&nbsp;</td>";
# ヘッダ、HTMLを出力
print "Content-type: text/html\n"
print "<html><body>"
print """<table border = "1"> %s </table>""" % b
print "</body></html>"
