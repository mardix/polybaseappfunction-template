# To run the service in dev mode
# > sh run-dev.sh
#
export FLASK_ENV=development
export FLASK_APP=main.py
export FLASK_RUN_PORT=5001

# App specific vars
export APP_ENV=sit
export POLYBASE_URL=http://localhost:5000/_polybase
export POLYBASE_ACCESS_KEY="gAAAAABgRD-o7aF42sGVmDqFb9Xa-JZWT_-zpb9AK6SVIzo8e7c6ZzP5JZN2NBCoHiQdnBVjCPPDbwst1VrATXrZafjDDpZk4Gsn1CP2wImbLsHDRMh7lrt4sqE7QAfwdvppn3mPhZ-gACoTF33mTvBa2n_sQwh6NliqAAJ1EjP1O-SDfgFN7so="
export POLYBASE_WEBHOOK_SECRET_TOKEN="SECRET"
flask run