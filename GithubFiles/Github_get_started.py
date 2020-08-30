from github import Github
import json

git = Github("Add your personal token of github") #add token here then only program will run 

all_repo = list()       #for repo
all_users = list()

def getAllRepo():
    for repo in git.get_user().get_repos():
        details = dict()
        details['reponame'] = repo.name
        all_repo.append(details)
    return all_repo

def getUser():
    user = git.get_user()
    uname = user.login
    return uname
