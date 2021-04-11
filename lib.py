import re
import sys
import uuid
import json
import datetime
import requests


def run_function(fn_module, fn_name, *args, **kwargs):
    """
    Run functions
    
    Args:
        - fn_module: the module containing the functions 
        - fn_name: the function name
        - *args
        - **kwargs
    """
    if fn_name.startswith("_"):
        raise Exception("400: function is invalid")
    if hasattr(fn_module, fn_name):
        return getattr(fn_module, fn_name)(*args, **kwargs)
    else:
        raise Exception("404: function doesn't exist")


def require_post_method(request):
    """
    Check if the request is a POST
    """
    if request.method != "POST":
        raise Exception('This function requires a POST method')

def get_headers_auth_bearer(request):
    """
    Get the Authorization Bearer
    """
    if 'Authorization' not in request.headers:
        return None
    data = request.headers['Authorization']
    return str.replace(str(data), 'Bearer ', '').strip()

def split_list(lst, n):
    """
    Split a list in multiple n chunks
    
    Args:
        - lst: list
        - n: number
    
    Returns Yield successive n-sized chunks from lst.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
#------------------------------------------------------------------------------
# Rejam API
#
class RejamException(Exception): pass

class Rejam(object):
    """
    Rejam
    """

    def __init__(self, url, access_key):
        self.url = url
        self.access_key = access_key

    def __call__(self, *a, **kw):
        """
        Make use of the class as a function for simplicity

        Example:
          # create client
          rejam_client = Rejam(url, access_key)

          # inline
          rejam_client("STORE.GET", collection="abc", _key="xyz")

          # With many args
          many_args = {
            "collection": "xyz",
            "data": [

            ],
            "operations": [

            ]
          }
          rejam_client("STORE.SET", **many_args)

        Args:
          - *args
          - **kwargs

        Returns:
          - mixed
        """
        return self.call(*a, **kw)

    def call(self, action, **kw):
        """
        Execute the Rejam service call

        Args:
          - action: string - the action to perform
          - *kw: mixed 
        Returns:
          - mixed
        """
        url = self.url
        headers = {
            "X-REJAM-ACCESS-KEY": self.access_key
        }
        data = {
            **kw,
            "action": action
        }
        r = requests.post(url, json=data, headers=headers)
        if r.status_code == requests.codes.ok:
            return r.json()
        else:
            _d = r.json()
            if "error" in _d:
                msg = _d["error"]["message"]
            else:
                msg = "[%s]" % r.status_code
            raise RejamException(msg)  