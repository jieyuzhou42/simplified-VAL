from web_interface import WebInterface
import json


class HtnInterface:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.knowledge_base = json.load(file)
    
    def get_decomposition(self, i):
        return self.knowledge_base[i]

class ValAgent:
    def add_method_from_user_task(user_interface, user_task):
        user_subtasks = user_interface.ask_subtasks(user_task)


user_interface = WebInterface()
user_task = user_interface.request_user_task()
tasks = HtnInterface("knowledge_base.json")
ValAgent = ValAgent
# VAL interpret user task
# task = ValAgent.interprete(user_task)
decomposition = tasks.get_decomposition(0)
i = 1
while decomposition:
    confirm_result = user_interface.confirm_best_match_decomposition(decomposition)
    if confirm_result == "yes":
        decomposition = tasks.get_decomposition(i)
        print("decomposition",decomposition)
        i += 1
    elif confirm_result == "more options":
        decomposition = tasks.get_decomposition(3)
    elif confirm_result == "add method":
        ValAgent.add_method_from_user_task("plate soup")
        decomposition = tasks.get_decomposition(4)
