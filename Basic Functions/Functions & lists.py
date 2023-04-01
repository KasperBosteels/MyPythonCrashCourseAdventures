messages = ["message 1","message 2","message 3"]

def show_messages (listOfMessages):
    for message in listOfMessages:
        print(message)
def send_messages (listOfMessages):
    newListOfMessages=[]
    for message in listOfMessages:
        show_messages(listOfMessages)
    newListOfMessages[:]
    listOfMessages=[]
    return newListOfMessages
newListOfMessages = send_messages(messages[:])
