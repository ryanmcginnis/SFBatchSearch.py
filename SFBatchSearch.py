#!/usr/bin/python

from os import system
from sys import argv
from time import sleep as sleep
from webbrowser import open as urlopen

theFile = open(argv[1], 'r')
sfURL = "https://na15.salesforce.com/_ui/search/ui/UnifiedSearchResults?str="	

urlopen("https://login.salesforce.com") # need to MANUALLY log in first without SF's API
system('clear'); raw_input("Please log in to Salesforce. Press any key to continue.")

def main():
	try:
		for i in theFile.read().splitlines():
			urlopen(sfURL + i)
			print ("Searched for " + i)			
		print ("\nDone!\n")
	except: print("Something went wrong, or user cancelled! Bailing out...")
	
if __name__ == "__main__":
	main()
	
