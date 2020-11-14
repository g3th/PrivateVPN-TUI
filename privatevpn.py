#!/usr/bin/python3
# PrivateVPN TUI
# Kali Linux/Debian or any Terminal
# 1535

from bs4 import BeautifulSoup as BullShit
import requests, os, sys

c_codes={'Afghanistan': 'AF', 'Åland Islands': 'AX', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ', 'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas': 'BS', 'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 'Bolivia (Plurinational State of)': 'BO', 'Bonaire, Sint Eustatius and Saba': 'BQ', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Bouvet Island': 'BV', 'Brazil': 'BR', 'British Indian Ocean Territory': 'IO', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cabo Verde': 'CV', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Cayman Islands': 'KY', 'Central African Republic': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Christmas Island': 'CX', 'Cocos (Keeling) Islands': 'CC', 'Colombia': 'CO', 'Comoros': 'KM', 'Congo': 'CG', 'Congo, Democratic Republic of the': 'CD', 'Cook Islands': 'CK', 'Costa Rica': 'CR', "Côte d'Ivoire": 'CI', 'Croatia': 'HR', 'Cuba': 'CU', 'Curaçao': 'CW', 'Cyprus': 'CY', 'Czech Republic': 'CZ', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Dominican Republic': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Eswatini': 'SZ', 'Ethiopia': 'ET', 'Falkland Islands (Malvinas)': 'FK', 'Faroe Islands': 'FO', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF', 'French Southern Territories': 'TF', 'Gabon': 'GA', 'Gambia': 'GM', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Heard Island and McDonald Islands': 'HM', 'Holy See': 'VA', 'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran (Islamic Republic of)': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', "Korea (Democratic People's Republic of)": 'KP', 'Korea, Republic of': 'KR', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', "Lao People's Democratic Republic": 'LA', 'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Marshall Islands': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Mayotte': 'YT', 'Mexico': 'MX', 'Micronesia (Federated States of)': 'FM', 'Moldova': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands': 'NL', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger': 'NE', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'North Macedonia': 'MK', 'Northern Mariana Islands': 'MP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Palestine, State of': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines': 'PH', 'Pitcairn': 'PN', 'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'Réunion': 'RE', 'Romania': 'RO', 'Russia': 'RU', 'Rwanda': 'RW', 'Saint Barthélemy': 'BL', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Martin (French part)': 'MF', 'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Sint Maarten (Dutch part)': 'SX', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Georgia and the South Sandwich Islands': 'GS', 'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan': 'SD', 'Suriname': 'SR', 'Svalbard and Jan Mayen': 'SJ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syrian Arab Republic': 'SY', 'Taiwan': 'TW', 'Tajikistan': 'TJ', 'Tanzania, United Republic of': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands': 'TC', 'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'United Arab Emirates': 'AE', 'United Kingdom': 'UK', 'USA': 'US', 'United States Minor Outlying Islands': 'UM', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Venezuela (Bolivarian Republic of)': 'VE', 'Vietnam': 'VN', 'Virgin Islands (British)': 'VG', 'Virgin Islands (U.S.)': 'VI', 'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}


page="https://privatevpn.com/serverlist"
headers= {'User-Agent':'Mozilla 5.0'}
url=requests.get(page,headers=headers)
soup=BullShit(url.text,'html.parser')

def nations():
	os.system("clear")
	print("\033[32m\n------------------------------------------")
	print("--- \033[33mPrivate VPN Client for Kali Linux \033[32m----")
	print("------------------------------------------\033[37m\n")
	n=1;t=31
	while n<len(al)/2:
		if n == 12:
			print(str(n)+") "+str(al[n])+"   	| "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1
		if n == 24:
			print(str(n)+") "+str(al[n])+"         | "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1
		else:
			print(str(n)+") "+str(al[n])+" 		| "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1

def cities():
	os.system("clear")
	print("\033[32m------------------------------------------")
	print("--- \033[33mPrivate VPN Client for Kali Linux \033[32m----")
	print("------------------------------------------\033[37m\n")
	if al[ch] == "South Korea":
		al[ch]="Korea, Republic of"
	match_c=[lines for lines in countries if al[ch] in lines]					
	r=1;l=0
	while r<=len(match_c):
		print(str(r)+") ",end="")
		if al[ch] == "Singapore":
			match_c="Singapore"
			print(match_c)
			break
		else:
			print(str(match_c[l:r]).split("- ")[-1].split("\\n")[0].split("']")[0])
			l=l+1;r=r+1
	return match_c
	
with open("/home/user/Desktop/PrivatVPN/privatvpn.conf",'r') as conf:
	line=conf.readlines(1)
	conf.close()

servers=[];countries=[];a=[];b=[]
x=1;y=1;z=0
while x < 91:
	country=soup.findAll('td')[z].text
	countries.append(country)
	x=x+1;z=z+6
	server=soup.findAll('td')[y].text
	servers.append(server)
	y=y+6

for i in countries:
	a.append(i.split("-")[0].strip())
	b.append(i.split("-")[-1].strip())

al=list(dict.fromkeys(a))
bl=list(dict.fromkeys(b))
while True:
	nations()
	ch=input("\n"+"\033[33mPick a country or (q)uit: ")
	if ch == "q":
		os.system("clear")
		exit()
	try:
		ch=int(ch)
		if ch > len(al) or ch ==0:
			os.system("clear")
		else: 
			while True:
				matchc=cities()
				ch1=input("\n"+"\033[33mPick a city, (p)revious or (q)uit: ")
				if ch1 == "q":
					os.system("clear")
					exit()
				if ch1 == "p":
					os.system("clear")
					break
				try:
					ch1=int(ch1)
					if ch1 > len(matchc) or ch1==0:
						os.system("clear")
					else:
						while True:
							city=str(matchc[ch1-1]).split("- ")[-1].split("\\n")[0]
							if len(city)<=2:
								city="Singapore"
							final=str(c_codes[al[ch]].lower())+"-"+city[:3].lower()+".pvdata.host"
							os.system("clear")
							print("\033[37mWill connect to "+city,end="");print(" in "+str(al[ch])+".")	
							endscript=input("\033[33m\nIs this correct (y/n)? \033[37")
							try:
								if endscript=="y":
									os.system("sed s/'"+str(*line).strip()+"'/'remote "+str(final)+" 1194 udp'/g /home/user/Desktop/PrivatVPN/privatvpn.conf > /home/user/Desktop/PrivatVPN/privatvpn2.conf")
									os.system("rm /home/user/Desktop/PrivatVPN/privatvpn.conf & mv /home/user/Desktop/PrivatVPN/privatvpn2.conf /home/user/Desktop/PrivatVPN/privatvpn.conf")
									os.system("sudo privatvpn")
									exit()
								if endscript=="n":
									print("Restarting...")
									os.execl(sys.executable, sys.executable, *sys.argv)
							except ValueError:
								os.system("clear")
				except ValueError:
					os.system("clear")
	except ValueError:
		os.system("clear")

