from class_to_test import Anonymous_survey

question = "what language did you first learn to speak?"
my_survey = Anonymous_survey(question)
my_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response = input("language: ")
    if response == 'q':
        break
    else:
        my_survey.store_response(response)
my_survey.show_results()

