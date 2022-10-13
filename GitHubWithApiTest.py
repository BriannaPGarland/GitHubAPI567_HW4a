from unittest.mock import Mock, patch
import GitHubWithApi
import unittest
import nose.tools
from nose.tools import assert_is_not_none, assert_is_none
import requests
import json

class GitHubWithAPITest(unittest.TestCase):
   
    #testing the call for the usr
    @patch('GitHubWithApi.get_usr_info')
    def test_good_call_to_API(self,mockGet):
        mockGet.returnValue.ok = True
        response = GitHubWithApi.get_usr_info('j-iuni')
        assert_is_not_none(response)
        
    @patch('GitHubWithApi.get_usr_info')
    def test_bad_call_to_API(self,mockGet):
        mockGet.returnValue.ok = False
        response = GitHubWithApi.get_usr_info('j-iuni')
        assert_is_not_none(response)
        
    #testing the call for the repo
    @patch('GitHubWithApi.get_repo_info')
    def test_good_call_for_repo(self,mockGet):
        mockGet.returnValue.ok = True
        response = GitHubWithApi.get_repo_info('j-iuni','CS583-A-Deep-Learning')
        assert_is_not_none(response)
#    # "Sorry, User ID entered was not found. Please try again" 
        
    #Testing Responses 
    @patch('GitHubWithApi.returnRepos')
    def test_full_function_call(self,mockGet):
        mockGet.return_value = ['Repo: CS583-A-Deep-Learning Number of commits: 1']
        response = GitHubWithApi.returnRepos("j-iuni")
        self.assertEqual(response, ['Repo: CS583-A-Deep-Learning Number of commits: 1'])
        
    @patch('GitHubWithApi.returnRepos')
    def test_full_function_call_2(self,mockGet):
        mockGet.return_value = "Error: No user ID was entered"
        response = GitHubWithApi.returnRepos("")
        self.assertEqual(response, "Error: No user ID was entered")    
        
    @patch('GitHubWithApi.returnRepos')
    def test_full_function_call_3(self,mockGet):
        mockGet.return_value =['Repo: ASL-Transcription Number of commits: 18', 'Repo: Brianna-Garland-SSW567 Number of commits: 30', 'Repo: CointCatcher2018 Number of commits: 13', 'Repo: ContactTracingApp-BackEnd Number of commits: 10', 'Repo: ContactTracingApp-FrontEnd Number of commits: 10', 'Repo: cpe490_go_project Number of commits: 5', 'Repo: Design6 Number of commits: 4', 'Repo: digitalSystemDesign Number of commits: 30', 'Repo: FlappyAttila Number of commits: 30', 'Repo: Form Number of commits: 15', 'Repo: FundamentalsOfSoft.PythonAssignments Number of commits: 7', 'Repo: GitHubAPI567_HW4a Number of commits: 6', 'Repo: HarvardCS50Lecture0 Number of commits: 5', 'Repo: helloworld Number of commits: 3', 'Repo: ImageProcImageSeg Number of commits: 7', 'Repo: ImageSegmentation Number of commits: 1', 'Repo: LanguageLearner Number of commits: 8', 'Repo: Reacting Number of commits: 1']
        response = GitHubWithApi.returnRepos("BriannaPGarland")
        self.assertEqual(response, ['Repo: ASL-Transcription Number of commits: 18', 'Repo: Brianna-Garland-SSW567 Number of commits: 30', 'Repo: CointCatcher2018 Number of commits: 13', 'Repo: ContactTracingApp-BackEnd Number of commits: 10', 'Repo: ContactTracingApp-FrontEnd Number of commits: 10', 'Repo: cpe490_go_project Number of commits: 5', 'Repo: Design6 Number of commits: 4', 'Repo: digitalSystemDesign Number of commits: 30', 'Repo: FlappyAttila Number of commits: 30', 'Repo: Form Number of commits: 15', 'Repo: FundamentalsOfSoft.PythonAssignments Number of commits: 7', 'Repo: GitHubAPI567_HW4a Number of commits: 6', 'Repo: HarvardCS50Lecture0 Number of commits: 5', 'Repo: helloworld Number of commits: 3', 'Repo: ImageProcImageSeg Number of commits: 7', 'Repo: ImageSegmentation Number of commits: 1', 'Repo: LanguageLearner Number of commits: 8', 'Repo: Reacting Number of commits: 1'])    
        
    @patch('GitHubWithApi.returnRepos')
    def test_full_function_call_4(self,mockGet):
        mockGet.return_value = ['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5']
        response = GitHubWithApi.returnRepos("richkempinski")
        self.assertEqual(response, ['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5'])     
