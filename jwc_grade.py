# this is a python program for scrawl the all semester grade in UESTC
# please filing the username and the password
# finish date: April 4th, 2016

import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup	
import lxml

filename = 'cookie.txt'
grade_htmlfile = 'grade_all.html'
# all_gradefilename = 'grade_all.txt'
# all_gradefile = open(all_gradefilename, 'w')
grade_html_open = open(grade_htmlfile, 'w')
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata_raw = {
			'username':'',		# filing the blank of your username
			'password':'',		# filing the blank of your password
			'dllt':'userNamePasswordLogin',
			'_eventId':'submit',
			'rmShown':'1',
			'lt': ' ',
			'execution': ' ',
		}
# print postdata, type(postdata)
loginUrl = 'http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal'
first_result = opener.open(loginUrl)			# first, get the lt and execution of the HTML
html = first_result.read()
soup = BeautifulSoup(html, 'lxml')
lt_string = str(soup.find_all('input')[2])
# print soup.find_all('input')
lt_value_raw = lt_string.split('=')[3]
# print lt_value_raw
lt_value = lt_value_raw.strip("\"").strip("\"/>")
postdata_raw['lt'] = lt_value
# print lt_value
execu_string = str(soup.find_all('input')[4])
execu_value_raw = execu_string.split('=')[-1]
execu_value = execu_value_raw.strip("\"").strip("\"/>")
postdata_raw['execution'] = execu_value
postdata = urllib.urlencode(postdata_raw)
# print postdata
loginUrl_login = 'http://idas.uestc.edu.cn/authserver/login' # the url for postdata
loginUrl_success = loginUrl+ '&' + postdata
print loginUrl_success
success_login_result = opener.open(loginUrl_success)
# second_urllib2_result = urllib2.urlopen(loginUrl_success)
# success_second_urllib2_html = second_urllib2_result.read()
# success_second_html = second_result.read()
# third_result = opener.open("http://portal.uestc.edu.cn/index.portal")
# success_third_html = third_result.read()
grade_all_url = 'http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR'
grade_all_result = opener.open(grade_all_url)
grade_all_html = grade_all_result.read() 
grade_html_open.write(grade_all_html)
grade_html_open.flush()
grade_html_open.close()
# post_result = opener.open()
# print excu_value

# print html
# cookie.save(ignore_discard=True, ignore_expires=True)

# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'

# result = opener.open(gradeUrl)
# print result.read()