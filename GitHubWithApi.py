import requests
import json
from pprint import pprint


# ID = input("What is your GitHub User ID")
# ID = input("What is your GitHub User ID?\n")
# print(ID)

ID="BriannaPGarland"

def returnRepos(ID):
    if ID != "": 
        try:
            url = f"https://api.github.com/users/{ID}/repos"
            userRepoList = requests.get(url).json()
        except: 
            print("Sorry, User ID entered was not found. Please try again")
        
        else:
            for i in range(len(userRepoList)):
                repoName=userRepoList[i]["name"]
                url = f"https://api.github.com/repos/{ID}/{repoName}/commits"
                listOfCommits = requests.get(url).json()
                numOfCommits=len(listOfCommits)
                print("Repo: "+repoName+" Number of commits: "+str(numOfCommits))
    else:
        print("Error: No user ID was entered")
returnRepos(ID)
