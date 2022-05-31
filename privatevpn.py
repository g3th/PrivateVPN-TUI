#!/usr/bin/python3
# Script to pick PrivateVPN server, write to conf
# and connect on Kali linux/any linux terminal
# Change directories to ones of your choice
# 1535

from bs4 import BeautifulSoup as BullShit
from countrycodes import c_codes
import requests, os, sys, time

page="https://privatevpn.com/serverlist"
headers= {'User-Agent':'Mozilla 5.0'}
url=requests.get(page,headers=headers)
soup=BullShit(url.text,'html.parser')

def nations():
	print("\n------------------------------------------")
	print("--- Private VPN Client for Kali Linux ----")
	print("------------------------------------------")
	n=1;t=31
	while n<len(al)/2:
		if n == 12:
			print(str(n)+") "+str(al[n])+"	| "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1
		if n == 24:
			print(str(n)+") "+str(al[n])+"         	| "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1
		if n == 25:
			print(str(n)+") "+str(al[n])+"		| "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1
		else:
			print(str(n)+") "+str(al[n])+" 		| "+str(t)+") "+str(al[t]))
			n=n+1;t=t+1

def cities():
	print("\n------------------------------------------")
	print("--- Private VPN Client for Kali Linux ----")
	print("------------------------------------------")
	if al[ch] == "South Korea":
		al[ch]="Korea, Republic of"
	match_c=[lines for lines in countries if al[ch] in lines]
	r=1;l=0
	while r<=len(match_c):
		print(str(r)+") ",end="")
		print(str(match_c[l:r]).split("- ")[-1].split("\\n")[0])
		l=l+1;r=r+1
	return match_c
	
with open("/home/roberto/Desktop/PrivateVPN/privatvpn.conf",'r') as conf:
	line=conf.readlines(1)
	conf.close()

servers=[];countries=[];a=[];b=[]
x=1;y=1;z=0
while x < 88:
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
	ch=input("\n"+"Pick a country or (q)uit: ")
	if ch == "q":
		os.system("clear")
		exit()
	try:
		ch=int(ch)
		if ch > len(al) or ch ==0:
			os.system("clear")
		else: 
			break
	except ValueError:
		os.system("clear")

while True:
	os.system("clear")
	matchc=cities()
	ch1=input("\n"+"Pick a city, (p)revious or (q)uit: ")
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
			break
	except ValueError:
		os.system("clear")

city=str(matchc[ch1-1]).split("- ")[-1].split("\\n")[0]	
final=str(c_codes[al[ch]].lower())+"-"+city[:3].lower()+".pvdata.host"
os.system("clear")
while True:
	print("Will connect to "+city,end="");print(" in "+str(al[ch])+".")
	endscript=input("\nIs this correct (y/n)? ")
	try:
		if endscript=="y":
			break
		if endscript=="n":
			print("Restarting...")
			os.execl(sys.executable, sys.executable, *sys.argv)
	except ValueError:
		os.system("clear")

os.system("sed s/'"+str(*line).strip()+"'/'remote "+str(final)+" 1194 udp'/g /home/roberto/Desktop/PrivateVPN/privatvpn.conf > /home/roberto/Desktop/PrivateVPN/privatvpn2.conf")
os.system("rm /home/roberto/Desktop/PrivatVPN/privatvpn.conf & mv /home/roberto/Desktop/PrivateVPN/privatvpn2.conf /home/roberto/Desktop/PrivateVPN/privatvpn.conf")
os.system("sudo privatvpn")
exit()
