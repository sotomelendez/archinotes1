# -*- coding: utf-8 -*-
import datetime,logging
from pymongo import MongoClient
logging.basicConfig(level=logging.DEBUG)

class Root():

	def __init__(self):
		pass

''' Init variables '''

DEVELOPMENT=True

POOL_SIZE=2000


if DEVELOPMENT == True:
  CONFIGURATION_FILE='development.cfg'
  DATABASE_ADDRESS='127.0.0.1'
  DATABASE_PORT=27017
else:
  CONFIGURATION_FILE='deployment.cfg'
  DATABASE_ADDRESS='ip'
  DATABASE_PORT=27017

CONFIGURATION_FOLDER='conf'

''' Generic response fields '''

MESSAGE='message'
EXPIRATION_DATE='expiration_date'
SUCCESS='success'

''' Web service variables '''

#Time to delete the token (seconds)
TIME_TO_DELETE_TOKEN = 900

#User token

USER_TOKEN='user-token'

KWARGS_TOKEN='token'

KWARGS_USER='user'

#JSON response template, it can not be a dict() because in memory all the clients will see the changes, we must create a clone
RESPONSE_TEMPLATE = (
  (MESSAGE,SUCCESS),
  (EXPIRATION_DATE,(datetime.datetime.utcnow()+datetime.timedelta(0,TIME_TO_DELETE_TOKEN)).strftime('%Y-%m-%d %H:%M:%S %Z'))
)

''' Database variables '''

#Connection to the database
CONNECTION=MongoClient(host=DATABASE_ADDRESS,port=DATABASE_PORT,max_pool_size=POOL_SIZE)

# User admin username
USER_USERNAME="archiproyecto"

# User Admin password
USER_PASSWORD="OneNote23f2014"

API_KEY='DFDFDFDF'


''' Exceptions '''

EXCEPTION_DATA_NONE = '%s_is_none'

EXCEPTION_DATA_NOT_EXISTS = '%s_not_exists'

EXCEPTION_DATA_ALREADY_EXISTS = '%s_already_exists'

EXCEPTION_DATA_BEING_USED = '%s_used'

EXCEPTION_USER_NOT_EXISTS = 'user_not_exists'

EXCEPTION_USER_NOT_ACTIVE = 'user_not_active'

EXCEPTION_BEGIN_DATE_LESS_FINISH_DATE = 'begin_date_is_greater_than_finish_date'

EXCEPTION_BEGIN_DATE_LESS_TODAY = 'begin_date_is_less_than_today'

EXCEPTION_PROCESSING_ERROR = 'server_processing_error'