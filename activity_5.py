import os
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_time():
	unix = str(time.time())
	final_string = "The current unix time is:" + unix

	return final_string

if __name__== "__main__":
	port = int(os.environ.get("PORT", 6738))
	app.run(host='0.0.0.0', port=port)