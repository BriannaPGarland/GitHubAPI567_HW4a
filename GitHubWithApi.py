import requests
import json
from pprint import pprint


# ID = input("What is your GitHub User ID")
# ID = input("What is your GitHub User ID?\n")
# print(ID)



def returnRepos(ID):
    listOfFinal=[]
    if ID != "": 
        try:
            url = f"https://api.github.com/users/{ID}/repos"
            userRepoList = requests.get(url).json()
        except: 
            return "Sorry, User ID entered was not found. Please try again"
        
        else:
            for i in range(len(userRepoList)):
                repoName=userRepoList[i]["name"]
                url = f"https://api.github.com/repos/{ID}/{repoName}/commits"
                listOfCommits = requests.get(url).json()
                numOfCommits=len(listOfCommits)
                listOfFinal.append("Repo: "+repoName+" Number of commits: "+str(numOfCommits))
                print("Repo: "+repoName+" Number of commits: "+str(numOfCommits))
            return (listOfFinal)
    else:
        return("Error: No user ID was entered")


