# Project Title:

Pool game score tracking app

## Prerequisites:

To run this project:
1. Python2 or 3
2. PostgreSQL
3. sqlalchemy
4. flask

## Files:
catalog folder:
	1. views.py
	2. model.py
	3. data.py
	template folder:
		1. main.html
		2. home.html
		3. play_game.html
		4. start_game.html
		5. create_player.html
		6. leaderboard.html
	static folder:
		1. styles.css
		2. app.js
		img folder:
			1. pool_body_bg.jpg

## How it works:

This project sets up a PostgreSQL database for a fictional pool
game score tracking web application. HTML, CSS and JavaScript 
uses to design front end functionality. The provided Python 
script uses the sqlalchemy library to create new player and read player
list from the database. After choosing two players from the list, 
user selects the winnera and python scripts update the statistics for 
both players involved in the game.

## Steps for running the program locally:

1. VirtualBox is the software that actually runs the virtual machine. 
   You can download it from virtualbox.org. Install the platform 
   package for your operating system.
2. Vagrant is the software that configures the VM and lets you share 
   files between your host computer and the VM's filesystem. Download it 
   from vagrantup.com. Install the version for your operating system.
3. The database is supplied inside catalog folder named itemcatalog.db or
	user can run the data.py file after 6th and 7th steps
5. Open a Linux-like command line terminal (e.g. Git Bash, MacOS terminal, etc.) 
6. Start the virtual machine using command 
			vagrant up
7. Login to the VM using 
			vagrant ssh
8. Using cd command go to the path where views.py was saved
9. Enter the following command to execute the program
			python views.py
10. Open a browser and enter folloeing address in the browser
			http://localhost:5000
11. You can now use the app in your local machine

## Git access:

https://github.com/szasohel/pool_stats.git

## Created by:

Sayed Zahed Abdullah Sohel
