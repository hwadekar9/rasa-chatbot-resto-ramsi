from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
from web_chat_connector import WebChatInput, SocketInputChannel
import os


from flask import Flask, render_template
from flask_socketio import SocketIO



import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.before_first_request
def activate_job():
    def run_job():
        nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
        agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)


        input_channel = WebChatInput(static_assets_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static'))

        #agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
        agent.handle_channel(SocketInputChannel(5500, '/bot', input_channel))

    thread = threading.Thread(target=run_job)
    thread.start()

@app.route('/')
def sessions():
    return render_template('session.html')


if __name__ == "__main__":
    app.run()