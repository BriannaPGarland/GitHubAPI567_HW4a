import unittest
from GitHubWithApi import returnRepos

class GitHubWithAPITest(unittest.TestCase):
    def testStringInput(self):
        self.assertEquals(returnRepos(""), "Error: No user ID was entered", 'A Blank was sent through for the userID')
    def testValidID(self):
        self.assertEquals(returnRepos("asjdalsdkasasfsdasfsdgeeg"), "Sorry, User ID entered was not found. Please try again", "The User ID entered was not a valid one")
    def testVProgramOutput(self):
        self.assertEquals(returnRepos("BriannaPGarland"),"Repo: ASL-Transcription Number of commits: 18\nRepo: Brianna-Garland-SSW567 Number of commits: 30\nRepo: CointCatcher2018 Number of commits: 13\nRepo: ContactTracingApp-BackEnd Number of commits: 10\nRepo: ContactTracingApp-FrontEnd Number of commits: 10\nRepo: cpe490_go_project Number of commits: 5\nRepo: Design6 Number of commits: 4\nRepo: digitalSystemDesign Number of commits: 30\nRepo: FlappyAttila Number of commits: 30\nRepo: Form Number of commits: 15\nRepo: FundamentalsOfSoft.PythonAssignments Number of commits: 7\nRepo: HarvardCS50Lecture0 Number of commits: 5\nRepo: helloworld Number of commits: \nRepo: ImageProcImageSeg Number of commits: 7\nRepo: ImageSegmentation Number of commits: 1\nRepo: LanguageLearner Number of commits: 8\nRepo: Reacting Number of commits: 1" )
