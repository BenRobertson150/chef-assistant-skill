from mycroft import MycroftSkill, intent_file_handler,intent_handler


class ChefAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.chef.intent')
    def handle_assistant_chef(self, message):
        self.speak_dialog('assistant.chef')

    @intent_handler('add.new.recipe')
    def handle_add_new_recipe(self,message):
        self.speak.dialog('add.recipe')
        recipe_name = self.get_response('what.is.the.recipe.name')
        self.speak_dialog('confirm.recipe.name', {'recipe_name': recipe_name})

def create_skill():
    return ChefAssistant()



