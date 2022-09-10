from flask import Flask, render_template
from datetime import datetime
import serial
import json
import atexit
from apscheduler.schedulers.background import BackgroundScheduler


# We read and retun data from the json file.

readed_data = []
def get_json():
    with open('data.json',encoding='utf-8') as f:
        data = json.load(f)
    return data
        


# This function is used to do regular task such as reading port number 7 
# and getting the value of current sensor.
def getvalue():
    try:
        
        ser = serial.Serial(
                    port='COM7',
                    baudrate=115200,
                )
        global readed_data

        value = dict()
        data = []
        line = ser.readline()
        line = line[:-2].decode("utf-8")
        value["value"] = float(line)


        if(float(line)<1):

            value["date"] = round(datetime.timestamp(datetime.now())*1000)
           
            with open('data.json') as f:
                data = json.load(f)

            data.append(value)
            readed_data.append(data)
            
            with open('data.json', 'w') as f:

                json.dump(data, f,
                        indent=4,
                        separators=(',', ': '))


            with open('data.json', 'r') as f:
                data = json.load(f)
    except:
        pass

# This scheduler calls function of getvalue as background application
# in every 0.3 seconds , even though the the another task is running.

scheduler = BackgroundScheduler()
scheduler.add_job(func=getvalue, trigger="interval", seconds=0.3)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())


# Flask section is starting here because we want to send the data to the server.

app = Flask(__name__)

# Routes for getting related information from the server.

@app.route('/')
def index():
    with open('data.json', encoding='utf-8') as f:
        data = f.read(999999)

    
    return render_template('index.html', jsonfile=data)


@ app.route('/graph')
def hello():

    with open('data.json') as f:
        data = json.load(f)

    return render_template('Graph.html', jsonfile=data)
   



app.run(host='192.168.4.224', debug=True)
