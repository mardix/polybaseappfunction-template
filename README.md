
# Polybase//AppFunction

It's a broke-man functions based api service to power your applications. 


---

### Usage

Domain: `https://[appname].polybaseapps.io`

#### Run functions over HTTP
```
https://[appname].polybaseapps.io?fn=[function_name]
```

#### Run functions over command line

```
python main.py --fn=[function_name] 
```

---

### Structure & files

Base structure:

```
|- main.py
|- functions.py
|- config.py
|- lib.py

```


#### main.py

`main.py` the entry point for HTTP and CLI access

#### config.py  

`config.py` contains application's configuration to be passed 

#### functions.py

`functions.py` contains all the functions to be executed. 


```
# functions.py

def hello_world(*args, **kwargs):
  #
  # simple function
  #
  return {
    "test": True
  }


def test_email(*a, **kw):
  #
  # in http, `flask.request` is passed as `request` in kw -> kw['request']
  #
  request = kw["request"]
  email = request.args.get("email")
  return {
    "email": email
  }
  
def test_email_2(*a, **kw):
  #
  # This can use args from request or from a kw[] value
  #
  
  email = None
  if "email" in kw:
    email = kw["email"]
  elif "request" in kw and "email" in kw["request"].args:
    email = kw["request"].args.get("email")
  
  # Throwing errors
  else:
    raise Exception('invalid email')
    
  # Retun the data
  return {
    "email": email
  }
  
```

---

### Setup

#### Requirements

Python:
- 3.6+

Framework:
- Flask

Local Env:
- pipenv 
- direnv

Deployment:
- Polybox



---

### Git and deploy

#### 1. Init

Initialize git `git init` 
 
#### 2. Add Remote Origin/Github

`git remote add origin git@github.com:mardix/[appname].polybaseapps.io.git`

#### 3. Add Remote Polybox

`git remote add polybox polybox@apps-01.polybaseapps.io:[appname].polybaseapps.io`

#### 4. Add DNS on AWS/Route53

Before pushing the initial code to polybox, that will automatically create the app, the domain must be registered and pointed to the right DNS box IP in. This is required for LetsEncrypt that will provide the free SSL.

#### 5. Deploy Site 

For each deployment, commit changes and push the code to `polybox` remote

`git push polybox master`

---

## Local Development

For local, use the command below.

Make sure you are in the right virtual env. `pipenv` and `direnv` are required

```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```

Or setup `run-dev.sh` 

```
# To run the service in dev mode
# > sh run-dev.sh
#
export FLASK_ENV=development
export FLASK_APP=main.py
export FLASK_RUN_PORT=5001

# App specific vars
export APP_ENV=sit
export POLYBASE_URL=http://localhost:5000/_polybase
export POLYBASE_ACCESS_KEY=""
export POLYBASE_WEBHOOK_SECRET_TOKEN=""
flask run
```

---

(c) 2021 - Mardix
