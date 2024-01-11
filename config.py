from os import environ

#TG Credentials
API_ID = int(environ.get('API_ID', '21159773'))
API_HASH = environ.get('API_HASH', '49ae08543a07335e195756eba2f56e11')
BOT_TOKEN = environ.get('BOT_TOKEN', '6600068998:AAGImvOOlm4j7HB01JAXVDcHkG9aVst1IsI')

#Website Credentials
API_KEY = environ.get('API_KEY', '5f82d8793633efb1268e8a4d3e7b4911e217d20a')
API_URL = environ.get('API_URL', 'https://pandaznetwork.com/api')
WEB_NAME = environ.get('WEB_NAME', 'PandazNetwork')

#Optional
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', 'https://t.me/pandaztalks')
UPDATES_CHANNEL = environ.get('UPDATES_CHANNEL', 'https://t.me/pandaznetwork')
