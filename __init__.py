from mycroft import MycroftSkill, intent_file_handler


class ChefAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.chef.intent')
    def handle_assistant_chef(self, message):
        self.speak_dialog('assistant.chef')


def create_skill():
    return ChefAssistant()

