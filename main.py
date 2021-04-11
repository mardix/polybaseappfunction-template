"""
Polybase//AppFunction
"""
import uuid
import datetime
import config
import traceback
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import click
import db
import lib
import functions

# ------------------------------------------------------------------------------
# HTTP
# Run functions from HTTP request
# /?fn=[fn_name]
# ------------------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object('config')
CORS(app)

@app.route('/', methods=["GET", "POST"])
def _http():
    if request.args.get("fn"):
        fn = request.args.get("fn")
        try:
            resp = lib.run_function(functions, fn, request=request)
            return jsonify({
                "data": resp
            })
        except Exception as e:
            return jsonify({
                "error": True,
                "message": str(e)
            }), 500      
    else:
        return "PolybaseAppFunction"


# ------------------------------------------------------------------------------
# CLI
# Run functions from command line
# python main.py --fn=[fn_name]
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    @click.command()
    @click.option("--fn", default=None, help="Function name")
    def _cli(fn):
        """
        To run a function
        """
        try:
            if fn:
                print(f"function: {fn}")
                resp = lib.run_function(functions, fn)
                print("results: ", resp)
                print("status: completed")
            else:
                print("-- PolybaseAppFunction --") 
        except Exception as e:
            print("error: ", e)    
            #traceback.print_exc()
    _cli()