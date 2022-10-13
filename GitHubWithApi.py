import requests
import json
from pprint import pprint


# ID = input("What is your GitHub User ID")
# ID = input("What is your GitHub User ID?\n")
# print(ID)

def get_usr_info(ID):
    try:
            url = f"https://api.github.com/users/{ID}/repos"
            userRepoList = requests.get(url).json()
            return userRepoList
    except: 
        return "Sorry, User ID entered was not found. Please try again"
    
def get_repo_info(ID,repoName):
    url = f"https://api.github.com/repos/{ID}/{repoName}/commits"
    listOfCommits = requests.get(url).json()
    return listOfCommits

def returnRepos(ID):
    listOfFinal =[]
    if ID != "": 
        userRepoList =get_usr_info(ID)
        for i in range(len(userRepoList)):
            repoName=userRepoList[i]["name"]
           
            listOfCommits = get_repo_info(ID, repoName)
            
            numOfCommits=len(listOfCommits)
            listOfFinal.append("Repo: "+repoName+" Number of commits: "+str(numOfCommits))
            print("Repo: "+repoName+" Number of commits: "+str(numOfCommits))
        return (listOfFinal)
    else:
        return("Error: No user ID was entered")



