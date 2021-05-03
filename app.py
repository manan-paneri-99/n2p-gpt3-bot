from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from n2pbot import convert, append_interaction_to_chat_log


app = Flask(__name__)
app.config['SECRET_KEY'] = '****************'

@app.route('/n2pbot', methods = ['POST'])
def n2pbot():
	incoming_msg = request.values['Body']
	chat_log = session.get('chat_log')

	point = convert(incoming_msg, chat_log)
	session['chat_log'] = append_interaction_to_chat_log(incoming_msg, point,
                                                         chat_log)
	r = MessagingResponse()
	r.message(point)
	return str(r)
