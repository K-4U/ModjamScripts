ModjamScripts
=============

Some scripts to use in your stream with Modjam!

Prerequisites:
==============
Githubv3 API for python:
[https://github.com/copitux/python-github3](https://github.com/copitux/python-github3)

Install:
========
Checkout the python-github3 and install that.

Place the streamScript.py in the directory where you want your files to be generated.

Config:
=======
Just edit the streamScript.py file. 
Lets take this github URL:
> https://github.com/K-4U/ModjamScripts

Your config would be this:

	nameOfRepository = "ModjamScripts"
	nameOfUser = "K-4U"

There isn't any more to it!

Note: As of now there is no option of where to place the textfiles!


Usage:
======
Just run the script with python:

> python streamScript.py