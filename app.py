from flask import Flask, render_template, request, jsonify
from pylgtv import WebOsClient
import sys, logging, time
from json import dumps

app = Flask(__name__)
#logging.basicConfig(stream=sys.stdout, level=logging.INFO)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/handler",methods=["GET","POST"])
def handler():
	try: code = request.args["code"]
	except: code = request.form["code"]
	tv = WebOsClient('IP')

	if code.startswith("ch") and len(code) > 2:
		channels = [i["channelId"] for i in tv.get_channels()]
		tv.set_channel(channels[int(code[2:])-1])

	elif code != "":
		code = int(code)

		if code == -3 :
			tv.power_on()

		elif code == -2 :
			tv.power_off()
	
		elif code == -1 :
			tv.set_mute(True if tv.get_muted() == False else False)
		
		elif code == 10 :
			tv.volume_up()
	
		elif code == 11 :
			tv.volume_down()
	
		elif code == 12 :
			tv.channel_up()
	
		elif code == 13 :
			tv.channel_down()

	response = jsonify(
		volume =tv.get_audio_status()["volume"],
		isMute = tv.get_audio_status()["mute"],
		channel = tv.get_current_channel()["channelNumber"]
	)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

if __name__ == "__main__":
	app.run(debug=True)
