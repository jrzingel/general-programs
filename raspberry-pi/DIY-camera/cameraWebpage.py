# Take a photo using the raspberry pi camera and display it on the screen

import os
from flask import *

MY_DIR = os.path.realpath(os.path.dirname(__file__))
STATIC = os.path.join(MY_DIR, 'static')

app = Flask(__name__)

# camera.capture(os.path.join(MY_DIR, 'image.jpg'))
# <img src="/static/image.jpg" alt="The image">

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/button', methods=['POST'])
def button():
    location = os.path.join(STATIC, 'image.jpg')
    command = 'raspistill -w 640 -h 480 -n -t 100 -q 10 -e jpg -th none -o ' + location
    print('Running command: ', command)
    os.system(command)
    return redirect(url_for('home'))


if __name__ == '__main__':
    print('* Running on http://cardix.local:5000/')
    app.run('0.0.0.0', 5000, debug=True)

'''<!--
<form action="/user/{{ username }}/button" method="post">
                <input type="submit" name="{{ 'buy' + mine }}" value="Buy mine">
            </form>
-->'''
