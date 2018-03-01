from bs4 import BeautifulSoup
import requests
import re

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","PQ","R","S","T","UV","WX","YZ"]

#resp = requests.get("http://www.dnd.kismetrose.com/CharacterNamesA.html")
#print resp
f = open("names.txt",'w')

def get_names_from_text(text):
	bs = BeautifulSoup(resp.text,"lxml")
	names= bs.find("table",{"dir":"LTR"}).text
	names = re.sub("\n+","",names)
	names = re.sub(" +"," ",names)
	names = names.strip()
	names = names.split(" ")
	names = "\n".join(names)
	names = names.encode("utf-8")
	return names

def make_request(letter):
	pref = "http://www.dnd.kismetrose.com/CharacterNames"
	suff = ".html"
	url = pref+letter+suff
	resp = requests.get(url)
	print resp
	return resp

def scrape_data():
	for letter in letters:
		resp = make_request(letter)
		names = get_names_from_text(resp.text)
		f.write(names+"\n")

	f.close()
