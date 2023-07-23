import json

class greeter():

    def __init__(self, filename):
        self.filename = filename

    def greet_user(self):
        try:
            with open ("../other_text_files/"+self.filename) as f:
                data = json.load(f)
                correct = input("Are you "+ data["username"] + "? (y/n) ")
                if(correct == "n"):
                    self.get_new_username()
                print("Welcome back, " + data["username"] + "!")
        except FileNotFoundError:
            self.get_new_username()

    def get_new_username(self):
        username = input("What is your name? ")
        with open ("../other_text_files/"+self.filename, 'w') as f:
            json.dump({"username":username}, f)
            print("We'll remember you when you come back, " + username + "!")



greeter = greeter("username.json")
greeter.greet_user()