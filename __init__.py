from mycroft import MycroftSkill, intent_file_handler


class Helloworld(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helloworld.intent')
    def handle_helloworld(self, message):
        self.speak_dialog('helloworld')


def create_skill():
    return Helloworld()

