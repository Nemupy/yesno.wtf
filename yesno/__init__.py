import requests


class YesNo:
    def __init__(self):
        response = requests.get("https://yesno.wtf/api")
        data = response.json()

        self.answer = data["answer"]
        self.forced = data["forced"]
        self.image = data["image"]

    def answer(self):
        return self.answer
    
    def forced(self):
        return self.forced
    
    def image(self):
        return self.image