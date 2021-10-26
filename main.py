from threading import Thread
from os import system

def run_flask():
    system('cd react/api; python3 app.py')

def run_react():
    system('cd react; yarn start')


def start():
    try:
        flask = Thread(target=run_flask)
        react = Thread(target=run_react)
    
        flask.start()
        react.start()
        
    except Exception:
        flask.stop()
        react.stop()


if __name__ == "__main__":
    start()
    while True:
        pass