#ModjamScripts
Some scripts to use in your stream with Modjam!

Sorry. There is no script (yet) for people who use bitbucket. They can simply disable the github lookup.
##Prerequisites

####For streamScript 
Githubv3 API for python:
[https://github.com/copitux/python-github3](https://github.com/copitux/python-github3)

###For commitScript
Only that you have Git installed and in your PATH. I don't know if Github for windows does this!

##Install
###For streamScript
Checkout the python-github3 and install that.

Place the streamScript.py in the directory where you want your files to be generated.

###For commitScript
Place it in a directory. Doesn't really matter.. (Not even in the end!)


##Config
###For streamScript
Just edit the streamScript.py file. 
Lets take this github URL:
> https://github.com/K-4U/ModjamScripts

Your config would be this:

	nameOfRepository = "ModjamScripts"
	nameOfUser = "K-4U"

If you don't want to check github every x minutes, set "checkForCommits" to False.

Note: As of now there is no option of where to place the textfiles!

###For commitScript
You only need to edit the path where your working copy is located.

For windows users: Use forward slashes.
So if your working copy is on 
>E:\Repositories\Modjam\

Your config will be this:

	repoDir = "E:/Repositories/Modjam"
There's also a print_debug. Set this to false if you don't want the script to print out messages about which files have changed.

##Usage
###For streamScript
Just run the script with python:

> python streamScript.py

Please take note that the Github API only allows for 60 requests every hour (per IP)! Do not change the timer at the bottom!

###For commitScript
The same. Just run the script with python:

> python commitScript.py

It'll print out the time that is left before making a commit. It will do this in minutes!

##Example
![](https://dl.dropboxusercontent.com/u/343724/MC/Modjam/streamScriptPreview.png)