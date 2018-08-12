# Joels Logs Analysis Project

This is a project I am coding to complete my Full Stack Nanodegree from udacity.com.
It will:
-Create a reporting tool that prints out reports based on the datat in the database.
-It is a Python program using the psycopg2 module to connect to the database.

## Download and Save

Create a folder on our PC and save these all of these files to it from my github repository:
https://github.com/jm2826/Joels-Logs-Analysis-Project.git

## Install

* Install - Version 2.7.15 from https://www.python.org/
* Install - Virtualbox from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
* Install - Vagrant from https://vagrantup.com
* Install - Git from https://git-scm.com/downloads
* Download - newsdata.zip file from Udacity.com (Fullstack Nanodegree ) Project: Logs Analysis Project


## Quickstart
*On your PC, search for Git Bash and open
* In the terminal, change directory to folder where newsdata zip file was saved.
* CD to vagrant
* Type: vagrant up enter enter
* Type: vagrant ssh then enter
* Type cd /vagrant
* CD to folder where your project folder is
* Run Python file by typing: python filename.py then enter

## Create View Statements
Instead of a complex psql query, I created to views for number 3. Here are the teo queries:

*create view num as SELECT to_char(time, 'yyyy-mm-dd') as date, count(*) FROM log where status like '404%' GROUP BY date;
*create view dem as SELECT to_char(time, 'yyyy-mm-dd') as date, count(*) FROM log GROUP BY date;

## Contributing
Please see CONTRIBUTING.md.
All files were originally written by udacity.com and modified by Joel Magee
