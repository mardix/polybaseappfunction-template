
# Functions

import os
import re
import uuid
import time
import datetime
import sys
import json
import slugify
import stream
#
import config
import lib
import db


#fn: hello
def hello(*a, **kw):
    return "Hello World"


#fn: test_post
def test_post(*a, **kw):
    """
    Test if it's a post call
    """
    if "request" in kw:
        lib.require_post_method(request=kw["request"])
    return "Success"   