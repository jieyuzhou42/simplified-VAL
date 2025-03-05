import socketio
from socketio.exceptions import TimeoutError
from typing import List
from typing import Optional


class WebInterface:

    def __init__(self, url="http://localhost:4002"):
        self.sio = socketio.Client()
        self.sio.connect(url)
        self.user_response = None
        self.response_received = False
        self.sio.on('message', self.on_message)
        
    def on_message(self, data):
        print("Received message:", data)
        if isinstance(data, dict) and 'response' in data:
            self.user_response = data['response']
            self.response_received = True 

    def request_user_task(self) -> str:
        self.user_response = None  
        self.response_received = False 

        self.sio.emit('message', {'type': 'request_user_task', 'text': 'How can I help you today?'})
        print("The message is emitted")
        while not self.response_received:
            self.sio.sleep(0.1)
        return self.user_response 
        
    def confirm_best_match_decomposition(self, best_match_decomposition: List[str]) -> bool:
        self.user_response = None  # Reset stored user response
        self.response_received = False  # Reset the response flag
        self.sio.emit('message', {'type': 'confirm_best_match_decomposition', 
                                  'text': best_match_decomposition})
        while not self.response_received:
            self.sio.sleep(0.1)
        print('received response:', self.user_response)
        return self.user_response
    
    def edit_decomposition(self,best_match_decomposition):
        """
        add_step()
        delete_step()
        change_order()
        change_pred()
        change_arg()
    
        """
        self.sio.emit('message', {'type': 'edit_decomposition', 
                                  'text': best_match_decomposition})
        print('sent confirmation')
        event = self.sio.receive()
        print('received event:', event[1])
        return
