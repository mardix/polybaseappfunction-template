import os 
from pathlib import Path

# The root dir
ROOT_DIR = Path(__file__).parent
APP_ENV = os.environ.get('APP_ENV', 'development').upper()
APP_NAME = "PolybaseAppFunction"

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#== PRODUCTION
if APP_ENV == 'PRODUCTION':
  DEBUG = False
  SECRET_KEY = ""
  REJAM_API_URL = ""
  REJAM_API_ACCESS_KEY = ""
  WEBHOOK_SECRET_TOKEN = ""
  

#== SIT
elif APP_ENV == 'SIT':
  DEBUG = False
  SECRET_KEY = ""
  REJAM_API_URL = ""
  REJAM_API_ACCESS_KEY = ""
  WEBHOOK_SECRET_TOKEN = ""
  
#== DEVELOPMENT
else:
  DEBUG = True
  SECRET_KEY = ""
  REJAM_API_URL = ""
  REJAM_API_ACCESS_KEY = ""
  WEBHOOK_SECRET_TOKEN = ""
