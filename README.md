# Fire Balloon Study Assistant

Run the following commands from the root directory to install requirements

    make
    virtualenv -p python3 venv
    . venv/bin/activate
    pip3 install -r requirements.txt

To run the front-end server, run the following command from the root directory.
    
    node app.js

To run the back-end server, run the following command from the root directory.
    
    FLASK_APP=9900_backend/app.py flask run