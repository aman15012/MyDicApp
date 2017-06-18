#Author: Aman Agarwal
#This is a simple dictionary application that scrapes the Dictionary.com to find relevant meanings for the entered word
#I was not able to add more features as the server was able to detect that the request was not from
# a browser and showed 404 Error for certain urls

from urllib.request import Request, urlopen 
from urllib.error import URLError, HTTPError
# urllib is used for establishing a connection with the dictionary.com server
from bs4 import BeautifulSoup
# beautifulsoup has been used parsng the html obtained from the request to dictionary,com

print("\nMyDicApp (Enter \"myDic\" to exit.)")
while(True):
	print()
	word = input("Enter the word: ")
	word=word.lower()
	if(word=="mydic"):
		exit()
	broken_word =  word.split(" ")
	word_size=len(broken_word)
	formatted_word = ""
	for i in range(len(broken_word)):
		formatted_word += broken_word[i]
		if(i<len(broken_word)-1):
			formatted_word += "-"
	url = "http://www.dictionary.com/browse/" + formatted_word + "?s=t";
	#url contains the required url, formatted accordingt ot the requirements
	req = Request(url)
	try:
		response = urlopen(req)
		#response contains the html page sent from the server as a response
	except HTTPError as e:
		print("Word not found :(")
	else:		
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		#parse the html
		def_list = soup.find_all("div", { "class" : "def-content" } )
		#extract the meaning
		if(len(def_list)>0):
			print("\nClosest Meaning(s):")
			for i in range(len(def_list)):
				if(i>=5):
					break
				print(str(i+1) + ". " + " ".join(def_list[i].text.split()))
		else:
			print("\nThis is a phrase. Use in a Sentence:")
			def_list = soup.find_all("p", { "class" : "def-text" } )
			print(" ".join(def_list[0].text.split()))

