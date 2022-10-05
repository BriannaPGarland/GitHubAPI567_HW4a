import unittest
from GitHubWithApi import returnRepos

class GitHubWithAPITest(unittest.TestCase):
# Passing
#     def testStringInput(self):
#         self.assertEquals(returnRepos(""), "Error: No user ID was entered", 'A Blank was sent through for the userID')
# NOT PASSING    
#     def testValidID(self):
#         self.assertEquals(returnRepos("asjdalsdkasasfsdasfsdgeeg"), "Sorry, User ID entered was not found. Please try again", "The User ID entered was not a valid one")
    
    def testVProgramOutput(self):
        self.assertEquals(returnRepos("BriannaPGarland"),['Repo: ASL-Transcription Number of commits: 18', 'Repo: Brianna-Garland-SSW567 Number of commits: 30', 'Repo: CointCatcher2018 Number of commits: 13', 'Repo: ContactTracingApp-BackEnd Number of commits: 10', 'Repo: ContactTracingApp-FrontEnd Number of commits: 10', 'Repo: cpe490_go_project Number of commits: 5', 'Repo: Design6 Number of commits: 4', 'Repo: digitalSystemDesign Number of commits: 30', 'Repo: FlappyAttila Number of commits: 30', 'Repo: Form Number of commits: 15', 'Repo: FundamentalsOfSoft.PythonAssignments Number of commits: 7', 'Repo: GitHubAPI567_HW4a Number of commits: 5', 'Repo: HarvardCS50Lecture0 Number of commits: 5', 'Repo: helloworld Number of commits: 3', 'Repo: ImageProcImageSeg Number of commits: 7', 'Repo: ImageSegmentation Number of commits: 1', 'Repo: LanguageLearner Number of commits: 8', 'Repo: Reacting Number of commits: 1'],"Success")
    
# Passing
#     def testProgrmOutput2(self):
#         self.assertEquals(returnRepos("j-iuni"), ['Repo: CS583-A-Deep-Learning Number of commits: 1'])    
