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
        steps = user_interface.segment_confirmation(user_subtasks)
        known_tasks = ['interact', 'go to']
        grounded_predicate = user_interface.map_correction(user_subtasks, known_tasks)


user_interface = WebInterface()

tasks = HtnInterface("knowledge_base.json")
ValAgent = ValAgent
# VAL interpret user task
# initial state:
# what does the start point looks like? current design is based on learned HTN knowledge/AI generated plan
# But when users 
user_task = user_interface.request_user_task()
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
        ValAgent.add_method_from_user_task(user_interface, "plate soup")
        decomposition = tasks.get_decomposition(4)
        # After rendering the chat box with VAL, VAL learns how to do the task. 
        # The HTN will send the same format decomposition to the front end, and then reactflow will render it.
    elif confirm_result == "edit":
        # 
        pass
    
