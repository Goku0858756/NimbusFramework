@PRE
## INSTALLED 	#############
mongoDB
Python3
python2

## START	#############
python nimbus.py
or
./nimbus.sh

## HELP 	#############
command: help
command: ?


## MODULES 	#############
crawl			Get into Crawl Shell Mode
target ——shell		Get into Target Shell Mode
scan ——shell		Get into Scanner Shell Mode
db			Database Controller
sqli			SQL Injection
web_gui			Start Web Control
			user | password
			test@user.com | secret

## CRAWLER|MODE	#############
	help or ?		For complete command list
	crawl help
	list			To get Current List of Targets from the Database
	list key:value		To filter targets from the database and get back in tables
				Example: list name:qi url:http://www.qi.nl
	list key:value crawl	Start the Crawling Directly	
	use			Crawler Help and Command Overview
	leave			Exit Crawler|Mode

## TARGET|MODE 	#############

	help or ?		For complete command list
	list			To get Current List of Targets from the Database
	list key:value		To filter targets from the database and get back in tables
				Example: list name:qi url:http://www.qi.nl
	list key:value save	Save to found Targets into the Current Active List of Targets to be used
	edit			This command is the List Targets and Edit/Update them
	edit key:value > key:value	
				Example: edit name:qi > name:qi-ict
	remove key:value	To Remove a Target from the Database.
				Confirmation will be asked before you delete the Target
	add			To Add a new Target
	add key:value key:value	
				Example: add ip:8.8.8.8 name:Google url:http://www.google.com
				Confirmation will be asked to “PIN” this target. Pinning means to use it right away
	leave			Exit Target|Mode

## DB		#############
	db ——start	To start the Database (MongoDB)
	db ——status	Check if Database is running
	db ——stop	Stop the Database

## SQL Inj.	#############
	

	Help:		sqli -h
	Start:		sqli -u [<target-url>]
	example:	sqli -u http://www.qi.nl	Start SQLi by URL
	example 2:	sqli -n qi			Start SQLi by name

## PLUGINS	#############
	
	exit the Framework and got to:
	cd Plugins/
	ls		Here you can find all Plugins Available for the Framework/Modules to 
	