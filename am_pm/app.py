from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])



def index():

    if request.method == 'POST':
        return return_AM_PM()

    else:
        pass

    return render_template('index.html')



def return_AM_PM():

    time_now = datetime.utcnow().time()
    hour_now = int(str(time_now)[:2])
    is_AM_now = bool(hour_now < 12)

    message_dict = {True:  'It is AM now',
                    False: 'It is PM now'}

    return message_dict[is_AM_now]



if __name__ == '__main__':

    app.run(debug=True)