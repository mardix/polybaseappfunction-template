# To run the service in dev mode
# > sh run-dev.sh
#
export FLASK_ENV=development
export FLASK_APP=main.py
export FLASK_RUN_PORT=5001

# App specific vars
export APP_ENV=development
flask run