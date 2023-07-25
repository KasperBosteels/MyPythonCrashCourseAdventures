import unittest
from class_to_test import Anonymous_survey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = "what language did you learn to speak first?"
        self.my_survey = Anonymous_survey(question)
        self.responses = ['English', 'Spanish', 'Dutch', 'German', 'French']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
