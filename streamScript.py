# Author: K-4U
# Written for Modjam 3
# Writes to two files: timeRemaining.txt and lastCommit.txt
# These files can then be read with your broadcasting software



#Config:

nameOfRepository = "The name of your repository on github"
nameOfUser = "The name of the user that owns the repository"


# DO NOT CHANGE ANYTHING BELOW THIS LINE UNLESS YOU KNOW WHAT YOU ARE DOING!
import time
import datetime as dt
import urllib2
import simplejson

lastTimeChecked = 0


githubRepoReq = urllib2.Request("https://api.github.com/repos/%s/%s"%(nameOfUser, nameOfRepository));
githubCommitReq = urllib2.Request("https://api.github.com/repos/%s/%s/commits/HEAD"%(nameOfUser, nameOfRepository))
githubOpener = urllib2.build_opener()


def calculateTimeLeft():
    endDate = dt.datetime(2013,12,17,05,59,59).replace(microsecond=0);
    dateNow = dt.datetime.now().replace(microsecond=0);

    td = (endDate-dateNow)

    # print("Time left: %s!"%td);

    outputFile = open('timeRemaining.txt','w')
    outputFile.write("Time left: %s!"%td)
    outputFile.close()

def getLatestCommit(lastTimeChecked):
    # f = githubOpener.open(githubRepoReq)
    # t = simplejson.load(f)
    t = {}
    t['pushed_at'] = "2013-12-08T12:29:39Z"
    if not (lastTimeChecked == t['pushed_at']):
        lastTimeChecked = t['pushed_at']
        #Get last commit:
        f = githubOpener.open(githubCommitReq)
        lastCommit = simplejson.load(f)
        #Write to file
        # lastCommit = {'commit':{"message":"test","committer":{"name":"Koen Beckers"}}}

        outputString = "Last commit: %i minutes ago by %s: %s"
        message = lastCommit['commit']["message"]
        committer = lastCommit['commit']["committer"]["name"]
        commitTime = time.mktime(time.strptime(lastTimeChecked, "%Y-%m-%dT%H:%M:%SZ")) #Time in GMT
        timeNow = time.mktime(time.gmtime())
        timeAgo = (timeNow-commitTime)

        timeAgo = timeAgo / 60;

        outputString = outputString % (timeAgo, committer, message)

        # print(outputString)
        
        outputFile = open('lastCommit.txt', 'w')
        outputFile.write(outputString)
        outputFile.close()

    return lastTimeChecked


count = 0
while(1):
    time.sleep(1)
    calculateTimeLeft()
    if((count % 120) == 0):
        lastTimeChecked = getLatestCommit(lastTimeChecked)
