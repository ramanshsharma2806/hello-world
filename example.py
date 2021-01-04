'''
today we will print hello world
'''

import requests
import json


class Coder:
    """
    our class that will invoke the amazing API's that we made earlier
    """
    
    def __init__(self):
        self.send_stuff = {'hey': 'give me hello world'}
        self.link = "https://hello-worldapi.herokuapp.com/"

    def print_this(f):
        def wrapped(self):
            print(f(self))
        
        return wrapped

    @print_this
    def show_what_is_on_root(self):
        return requests.post(self.link).text
    
    @print_this
    def get_hello_world(self):
        return json.loads(requests.post(self.link+'/hello_world', self.send_stuff).text)['response']
        

not_you = Coder()

not_you.show_what_is_on_root()
not_you.get_hello_world()